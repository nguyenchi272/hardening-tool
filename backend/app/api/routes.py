from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from pydantic import BaseModel
import asyncio

from app.services.linux_audit \
    import LinuxAudit

from app.services.dynamic_audit_engine \
    import DynamicAuditEngine

from app.services.realtime_scan \
    import RealtimeScanService

from sqlalchemy.orm \
    import Session

from sqlalchemy import func

from app.db.session \
    import get_db

from app.services.persistence_service \
    import PersistenceService

from app.db.database \
    import SessionLocal

from app.db.models.scan \
    import Scan

from app.db.models.asset \
    import Asset

from app.db.models.finding \
    import FindingRecord

from fastapi.responses \
    import FileResponse

from app.services.report_service \
    import ReportService

from app.services.remediation_service \
    import RemediationService

router = APIRouter(
    prefix="/api/v1"
)

LATEST_FINDINGS = []


class ScanRequest(BaseModel):
    host: str
    username: str
    password: str

class FixRequest(BaseModel):

    host: str

    username: str

    password: str

    finding_id: str

@router.get("/health")
def health():
    return {
        "status": "ok"
    }


@router.get("/findings")
def get_findings():

    return LATEST_FINDINGS

@router.post("/scan")
def start_scan(
    payload: ScanRequest,
    db: Session = Depends(get_db)
):

    global LATEST_FINDINGS

    audit = LinuxAudit(
        payload.host,
        payload.username,
        payload.password
    )

    collected_data = \
        audit.collect()

    engine = DynamicAuditEngine()

    findings = engine.run(
        collected_data
    )

    LATEST_FINDINGS = findings
    PersistenceService().save_scan(
        db,
        payload.host,
        findings,
        collected_data
    )

    return {
        "status": "completed",
        "target": payload.host,
        "findings": findings,
        "raw_data": collected_data
    }

@router.websocket("/ws/scan")
async def websocket_scan(
    websocket: WebSocket
):

    await websocket.accept()

    try:

        data = \
            await websocket.receive_json()

        hosts = data["hosts"]

        username = data["username"]

        password = data["password"]

        scanner = \
            RealtimeScanService(
                websocket
            )

        #
        # Run multi-host scan
        #
        results = \
            await scanner.run_multi_scan(
                hosts,
                username,
                password
            )

        #
        # Save all findings
        #
        db = SessionLocal()

        all_findings = []

        for result in results:

            #
            # Skip failed hosts
            #
            if isinstance(
                result,
                Exception
            ):
                continue

            host = \
                result["host"]

            findings = \
                result["findings"]

            collected_data = \
                result["collected_data"]

            PersistenceService().save_scan(
                db,
                host,
                findings,
                collected_data
            )

            all_findings.extend(
                findings
            )

        db.close()

        global LATEST_FINDINGS

        LATEST_FINDINGS = all_findings

        await websocket.send_json({

            "type": "completed",

            "findings_count":
                len(all_findings)
        })

    except WebSocketDisconnect:

        print(
            "Client disconnected"
        )

    except Exception as e:

        await websocket.send_json({

            "type": "error",

            "message": str(e)
        })

    finally:

        try:
            await websocket.close()

        except:
            pass

@router.get("/dashboard/findings")
def dashboard_findings(
    db: Session = Depends(get_db)
):

    findings = (
        db.query(
            FindingRecord,
            Asset.hostname,
            Asset.ip_address
        )
        .join(
            Scan,
            FindingRecord.scan_id == Scan.id
        )
        .join(
            Asset,
            Scan.asset_id == Asset.id
        )
        .all()
    )

    results = []

    for finding, hostname, ip_address in findings:

        results.append({

            "id":
                str(finding.id),

            "finding_id":
                finding.finding_id,

            "title":
                finding.title,

            "severity":
                finding.severity,

            "risk_score":
                8,

            "category":
                "Security",

            "description":
                "",

            "impact":
                "",

            "evidence":
                finding.evidence,

            "remediation":
                finding.remediation,

            "references":
                [],

            "compliance":
                [],

            "tags":
                [],

            "server":
                hostname,

            "ip_address":
                ip_address,

            "status":
                finding.status
        })

    return results

@router.get("/dashboard/assets")
def dashboard_assets(
    db: Session = Depends(get_db)
):

    assets = (
        db.query(Asset)
        .all()
    )

    results = []

    for asset in assets:

        findings_count = (
            db.query(FindingRecord)
            .join(
                Scan,
                Scan.id ==
                FindingRecord.scan_id
            )
            .filter(
                Scan.asset_id ==
                asset.id
            )
            .count()
        )

        results.append({

            "id": asset.id, 

            "hostname":
                asset.hostname,

            "ip_address":
                asset.ip_address,

            "os":
                asset.os,

            "findings":
                findings_count,

            "risk":
                findings_count * 10
        })

    return results

@router.get("/dashboard/compliance")
def dashboard_compliance(
    db: Session = Depends(get_db)
):

    findings = (
        db.query(FindingRecord)
        .all()
    )

    cis_failed = 0
    pci_failed = 0
    nist_failed = 0

    for finding in findings:

        title = (
            finding.title.lower()
        )

        if (
            "ssh" in title
            or "selinux" in title
            or "firewalld" in title
        ):
            cis_failed += 1

        if (
            "password" in title
            or "authentication" in title
        ):
            pci_failed += 1

        nist_failed += 1

    cis_score = max(
        100 - (cis_failed * 5),
        0
    )

    pci_score = max(
        100 - (pci_failed * 5),
        0
    )

    nist_score = max(
        100 - (nist_failed * 3),
        0
    )

    return [

        {
            "framework":
                "CIS Oracle Linux",

            "score":
                cis_score,

            "failed_controls":
                cis_failed,

            "status":
                (
                    "Compliant"
                    if cis_score >= 80
                    else "At Risk"
                )
        },

        {
            "framework":
                "PCI-DSS",

            "score":
                pci_score,

            "failed_controls":
                pci_failed,

            "status":
                (
                    "Compliant"
                    if pci_score >= 80
                    else "At Risk"
                )
        },

        {
            "framework":
                "NIST",

            "score":
                nist_score,

            "failed_controls":
                nist_failed,

            "status":
                (
                    "Compliant"
                    if nist_score >= 80
                    else "At Risk"
                )
        }
    ]

@router.get("/dashboard/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):

    findings = (
        db.query(FindingRecord)
        .all()
    )

    assets = (
        db.query(Asset)
        .all()
    )

    critical = len([
        f for f in findings
        if f.severity == "Critical"
    ])

    high = len([
        f for f in findings
        if f.severity == "High"
    ])

    medium = len([
        f for f in findings
        if f.severity == "Medium"
    ])

    low = len([
        f for f in findings
        if f.severity == "Low"
    ])

    total_risk = (
        critical * 10
        + high * 7
        + medium * 4
        + low * 2
    )

    return {

        "assets":
            len(assets),

        "findings":
            len(findings),

        "critical":
            critical,

        "high":
            high,

        "medium":
            medium,

        "low":
            low,

        "risk_score":
            total_risk
    }

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

@router.get(
    "/reports/asset/{asset_id}"
)
def export_asset_report(
    asset_id: int,
    db: Session = Depends(get_db)
):

    pdf_path = \
        ReportService().generate_asset_report(
            db,
            asset_id
        )

    return FileResponse(
        pdf_path,
        media_type=
            "application/pdf",
        filename=
            f"asset_{asset_id}_report.pdf"
    )

@router.post("/fix")
def fix_finding(
    payload: FixRequest
):

    result = \
        RemediationService().fix_finding(

            payload.host,

            payload.username,

            payload.password,

            payload.finding_id
        )

    return result