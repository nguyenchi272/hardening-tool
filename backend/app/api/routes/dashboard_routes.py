from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session \
    import get_db
from app.db.models.asset import Asset
from app.db.models.finding import FindingRecord
from app.db.models.scan import Scan


router = APIRouter()

@router.get("/dashboard/findings")
def dashboard_findings(
    db: Session = Depends(get_db)
):

    findings = (
        db.query(
            FindingRecord,
            Asset.id,
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

    for finding, asset_id, hostname, ip_address in findings:

        results.append({

            "id":
                str(finding.id),

            "asset_id":
                asset_id,

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
                finding.status,

            "auto_fix_supported":
                finding.auto_fix_supported,

            "requires_restart":
                finding.requires_restart,

            "requires_reboot":
                finding.requires_reboot,

            "manual_review":
                finding.manual_review
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