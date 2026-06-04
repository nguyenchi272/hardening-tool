from app.services.auditors.base_audit \
    import BaseAudit



class UbuntuAudit(BaseAudit):


    def collect(self):

        data = {}


        data.update(
            self.collect_common()
        )


        commands = {


            "os_release":
                "cat /etc/os-release",


            #
            # AppArmor
            #

            "apparmor":
                "aa-status 2>/dev/null",


            #
            # Firewall
            #

            "ufw":
                "ufw status 2>/dev/null",


            "nftables":
                (
                    "systemctl is-active "
                    "nftables 2>/dev/null"
                ),


            #
            # Package
            #

            "apt_packages":
                "dpkg -l",


            #
            # Ubuntu update
            #

            "unattended_upgrades":

                (
                "systemctl is-enabled "
                "unattended-upgrades "
                "2>/dev/null"
                )

        }


        data.update(
            self.execute_commands(
                commands
            )
        )


        return data