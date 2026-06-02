from app.services.auditors.base_audit \
    import BaseAudit


class RHELAudit(BaseAudit):

    def collect(self):

        commands = {

            #
            # Identity
            #
            "host":
                "hostname -I | awk '{print $1}'",

            "hostname":
                "hostname",

            "os_release":
                "cat /etc/os-release",

            #
            # SSH
            #
            "sshd_config":
                "cat /etc/ssh/sshd_config",

            #
            # Password Policy
            #
            "login_defs":
                "cat /etc/login.defs",

            "pwquality":
                "cat /etc/security/pwquality.conf",

            #
            # SELinux
            #
            "selinux":
                "getenforce",

            #
            # Firewall
            #
            "firewalld":
                "systemctl is-active firewalld",

            #
            # Audit
            #
            "auditd":
                "systemctl is-active auditd",

            "audit_rules":
                "cat /etc/audit/audit.rules 2>/dev/null",

            #
            # Logging
            #
            "rsyslog":
                "systemctl is-active rsyslog",

            "journald":
                "systemctl is-enabled systemd-journald",

            #
            # Kernel
            #
            "sysctl":
                "sysctl -a 2>/dev/null",

            #
            # Services
            #
            "services":
                "systemctl list-units --type=service",

            "enabled_services":
                "systemctl list-unit-files --type=service --state=enabled",

            #
            # Network
            #
            "open_ports":
                "ss -tulnp",

            #
            # Packages
            #
            "installed_packages":
                "rpm -qa",

            #
            # Filesystem
            #
            "mounts":
                "mount",

            "passwd_perm":
                "stat -c '%a' /etc/passwd",

            "shadow_perm":
                "stat -c '%a' /etc/shadow",

            "gshadow_perm":
                "stat -c '%a' /etc/gshadow",

            "crontab_perm":
                "stat -c '%a %U %G' /etc/crontab",

            #
            # World writable
            #
            "world_writable":
                (
                    "find / -xdev "
                    "-type f "
                    "-perm -0002 "
                    "2>/dev/null | head -50"
                )
        }

        return self.execute_commands(
            commands
        )