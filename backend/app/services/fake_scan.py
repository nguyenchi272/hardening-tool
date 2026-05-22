from app.models.finding import Finding


def generate_fake_findings():
    return [
        Finding(
            id=1,
            finding_id="SSH-001",
            title="Root Login Enabled",
            severity="High",
            description="SSH root login is enabled",
            server="ol8-prod"
        ),
        Finding(
            id=2,
            finding_id="AUTH-001",
            title="Weak Password Policy",
            severity="Medium",
            description="Password policy is weak",
            server="db01"
        ),
        Finding(
            id=3,
            finding_id="FW-001",
            title="Firewall Disabled",
            severity="Critical",
            description="firewalld service is disabled",
            server="oracle-app"
        ),
        Finding(
            id=4,
            finding_id="DBS-001",
            title="Oracle database server",
            severity="Medium",
            description="Database is opened",
            server="oracle-app"
        ),
    ]