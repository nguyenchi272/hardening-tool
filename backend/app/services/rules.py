from app.core.finding_factory \
    import create_finding


def check_root_login(
    sshd_config,
    server
):
    findings = []

    if (
        "PermitRootLogin no"
        not in sshd_config
    ):

        findings.append(
            create_finding(
                finding_id="SSH-001",

                title=
                    "Root Login Enabled",

                severity="High",

                category="SSH",

                description=
                    """
                    SSH root login is enabled.
                    Attackers may brute-force
                    privileged accounts.
                    """,

                impact=
                    """
                    Full server compromise
                    possible if credentials
                    are leaked.
                    """,

                evidence=
                    """
                    PermitRootLogin no
                    not found in
                    sshd_config.
                    """,

                remediation=
                    """
                    Edit:
                    /etc/ssh/sshd_config

                    Set:
                    PermitRootLogin no

                    Restart SSH:
                    systemctl restart sshd
                    """,

                references=[
                    "CIS Oracle Linux Benchmark",
                    "NIST 800-53"
                ],

                compliance=[
                    "CIS-5.2.8",
                    "NIST-AC-6"
                ],

                tags=[
                    "ssh",
                    "authentication",
                    "hardening"
                ],

                server=server
            )
        )

    return findings


def check_selinux(
    selinux,
    server
):
    findings = []

    selinux = \
        selinux.strip().lower()

    if selinux != "enforcing":

        findings.append(
            create_finding(
                finding_id=
                    "SELINUX-001",

                title=
                    "SELinux Not Enforcing",

                severity="High",

                category="SELinux",

                description=
                    """
                    SELinux is not
                    running in enforcing mode.
                    """,

                impact=
                    """
                    Mandatory access control
                    protections are weakened.
                    """,

                evidence=
                    f"SELinux state: {selinux}",

                remediation=
                    """
                    Set SELINUX=enforcing
                    in:

                    /etc/selinux/config
                    """,

                references=[
                    "Oracle Linux Security Guide"
                ],

                compliance=[
                    "CIS-1.6.1"
                ],

                tags=[
                    "selinux",
                    "mac",
                    "hardening"
                ],

                server=server
            )
        )

    return findings


def check_firewalld(
    firewalld,
    server
):
    findings = []

    firewalld = \
        firewalld.strip().lower()

    if firewalld != "active":

        findings.append(
            create_finding(
                finding_id="FW-001",

                title=
                    "Firewall Disabled",

                severity="Critical",

                category="Firewall",

                description=
                    """
                    firewalld service
                    is not active.
                    """,

                impact=
                    """
                    Server exposed directly
                    to network attacks.
                    """,

                evidence=
                    f"firewalld state: {firewalld}",

                remediation=
                    """
                    Enable firewalld:

                    systemctl enable firewalld
                    systemctl start firewalld
                    """,

                references=[
                    "CIS Oracle Linux Benchmark"
                ],

                compliance=[
                    "CIS-3.4.2"
                ],

                tags=[
                    "firewall",
                    "network",
                    "hardening"
                ],

                server=server
            )
        )

    return findings