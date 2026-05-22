from app.services.ssh_collector \
    import SSHCollector


class LinuxAudit:

    def __init__(
        self,
        host,
        username,
        password
    ):
        self.collector = SSHCollector(
            host,
            username,
            password
        )

    def collect(self):

        self.collector.connect()

        data = {
            "hostname":
                self.collector.run_command(
                    "hostname"
                )["stdout"].strip(),

            "os_version":
                self.collector.run_command(
                    "cat /etc/os-release"
                )["stdout"].strip(),

            "sshd_config":
                self.collector.run_command(
                    "cat /etc/ssh/sshd_config"
                )["stdout"],

            "selinux":
                self.collector.run_command(
                    "getenforce"
                )["stdout"].strip(),

            "open_ports":
                self.collector.run_command(
                    "ss -tulnp"
                )["stdout"],

            "firewalld":
                self.collector.run_command(
                    "systemctl is-active firewalld"
                )["stdout"].strip(),
            
            "login_defs":
                self.collector.run_command(
                    "cat /etc/login.defs"
                )["stdout"],

            "pwquality":
                self.collector.run_command(
                    "cat /etc/security/pwquality.conf"
                )["stdout"],
            
            "installed_packages":
                self.collector.run_command(
                    "rpm -qa"
                )["stdout"],
            
            "services":
                self.collector.run_command(
                    "systemctl list-units --type=service"
                )["stdout"],

            "mounts":
                self.collector.run_command(
                    "mount"
                )["stdout"],

            "enabled_services":
                self.collector.run_command(
                    "systemctl list-unit-files --type=service --state=enabled"
                )["stdout"],

            "sysctl":
                self.collector.run_command(
                    "sysctl -a"
                )["stdout"],

            "passwd_perm":
                self.collector.run_command(
                    "stat -c '%a' /etc/passwd"
                )["stdout"],

            "shadow_perm":
                self.collector.run_command(
                    "stat -c '%a' /etc/shadow"
                )["stdout"],

            "gshadow_perm":
                self.collector.run_command(
                    "stat -c '%a' /etc/gshadow"
                )["stdout"],

            "world_writable":
                self.collector.run_command(
                    "find / -xdev -type f -perm -0002 2>/dev/null | head"
                )["stdout"],

            "auditd":
                self.collector.run_command(
                    "systemctl is-active auditd"
                )["stdout"],

            "rsyslog":
                self.collector.run_command(
                    "systemctl is-active rsyslog"
                )["stdout"],

            "journald":
                self.collector.run_command(
                    "systemctl is-enabled systemd-journald"
                )["stdout"],

            "audit_rules":
                self.collector.run_command(
                    "cat /etc/audit/audit.rules 2>/dev/null"
                )["stdout"],
        }

        self.collector.close()

        return data