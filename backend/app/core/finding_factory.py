from app.models.finding import Finding

from app.core.severity \
    import SEVERITY_SCORES


def create_finding(
    finding_id,
    title,
    severity,
    category,
    description,
    impact,
    evidence,
    remediation,
    server,
    references=None,
    compliance=None,
    tags=None
):

    return Finding(
        id=hash(finding_id),

        finding_id=finding_id,

        title=title,

        severity=severity,

        risk_score=
            SEVERITY_SCORES[
                severity
            ],

        category=category,

        description=description,

        impact=impact,

        evidence=evidence,

        remediation=remediation,

        references=references or [],

        compliance=compliance or [],

        tags=tags or [],

        server=server,

        status="Open"
    )