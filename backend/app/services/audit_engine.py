# audit_engine.py

from app.services.rules \
    import (
        check_root_login,
        check_selinux,
        check_firewalld
    )


class AuditEngine:

    def run(
        self,
        data
    ):

        findings = []

        hostname = \
            data.get(
                "hostname",
                "unknown"
            ).strip()

        sshd_config = \
            data.get(
                "sshd_config",
                ""
            )

        selinux = \
            data.get(
                "selinux",
                ""
            )

        firewalld = \
            data.get(
                "firewalld",
                ""
            )

        #
        # SSH Audit
        #
        ssh_findings = \
            check_root_login(
                sshd_config,
                hostname
            )

        findings.extend(
            ssh_findings
        )

        #
        # SELinux Audit
        #
        selinux_findings = \
            check_selinux(
                selinux,
                hostname
            )

        findings.extend(
            selinux_findings
        )

        #
        # Firewalld Audit
        #
        firewall_findings = \
            check_firewalld(
                firewalld,
                hostname
            )

        findings.extend(
            firewall_findings
        )

        #
        # Sort findings
        #
        severity_order = {
            "Critical": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1,
            "Info": 0
        }

        findings.sort(
            key=lambda x:
                severity_order.get(
                    x.severity,
                    0
                ),
            reverse=True
        )

        return findings