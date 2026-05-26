from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session \
    import get_db
from app.db.models.asset \
    import Asset
from app.db.models.finding import FindingRecord
from app.db.models.scan import Scan

router = APIRouter()


@router.get("/assets/{asset_id}")
def get_asset_detail(
    asset_id: int,
    db: Session = Depends(get_db)
):

    asset = db.query(
        Asset
    ).filter(
        Asset.id == asset_id
    ).first()

    if not asset:

        return {
            "error": "Asset not found"
        }

    latest_scan = db.query(
        Scan
    ).filter(
        Scan.asset_id == asset.id
    ).order_by(
        Scan.id.desc()
    ).first()

    findings = []

    if latest_scan:

        findings = db.query(
            FindingRecord
        ).filter(
            FindingRecord.scan_id ==
                latest_scan.id
        ).all()

    severity_count = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    risk_score = 0

    severity_score = {
        "Critical": 10,
        "High": 7,
        "Medium": 5,
        "Low": 2
    }

    for finding in findings:

        sev = finding.severity

        if sev in severity_count:

            severity_count[sev] += 1

        risk_score += \
            severity_score.get(
                sev,
                0
            )

    return {

        "asset": {

            "id": asset.id,

            "hostname":
                asset.hostname,

            "ip_address":
                asset.ip_address,

            "os":
                asset.os,

            "status":
                asset.status
        },

        "summary": {

            "findings":
                len(findings),

            "risk_score":
                risk_score,

            "severity":
                severity_count
        },

        "findings": [

            {

                "id":
                    finding.id,

                "finding_id":
                    finding.finding_id,

                "title":
                    finding.title,

                "severity":
                    finding.severity,

                "evidence":
                    finding.evidence,

                "remediation":
                    finding.remediation,

                "status":
                    finding.status
            }

            for finding in findings
        ]
    }