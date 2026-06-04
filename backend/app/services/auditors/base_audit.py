class BaseAudit:

    def __init__(
        self,
        ssh
    ):
        self.ssh = ssh


    def execute_commands(
        self,
        commands
    ):

        data = {}

        for key, cmd in commands.items():

            try:

                result = self.ssh.run_command(
                    cmd
                )

                data[key] = (
                    result["stdout"]
                    .strip()
                )

            except Exception as e:

                data[key] = ""

                print(
                    f"[AUDIT ERROR] {key}: {e}"
                )

        return data


    def collect_common(self):

        commands = {

            #
            # Identity
            #

            "hostname":
                "hostname",

            "host":
                "hostname -I | awk '{print $1}'",


            #
            # SSH
            #

            "sshd_config":
                "cat /etc/ssh/sshd_config",


            #
            # Password
            #

            "login_defs":
                "cat /etc/login.defs",

            "pwquality":
                "cat /etc/security/pwquality.conf 2>/dev/null",


            #
            # Kernel
            #

            "sysctl":
                "sysctl -a 2>/dev/null",


            #
            # Logging
            #

            "auditd":
                "systemctl is-active auditd",

            "rsyslog":
                "systemctl is-active rsyslog",

            "journald":
                "systemctl is-enabled systemd-journald",


            #
            # Network
            #

            "open_ports":
                "ss -tulnp",


            #
            # Services
            #

            "services":
                "systemctl list-units --type=service",

            "enabled_services":
                (
                    "systemctl list-unit-files "
                    "--type=service "
                    "--state=enabled"
                ),


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