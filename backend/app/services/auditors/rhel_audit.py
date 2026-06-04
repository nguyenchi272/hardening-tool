from app.services.auditors.base_audit \
    import BaseAudit



class RHELAudit(BaseAudit):


    def collect(self):


        data = {}


        #
        # Common CIS
        #

        data.update(
            self.collect_common()
        )


        #
        # RHEL specific
        #

        commands = {


            "os_release":
                "cat /etc/os-release",


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
            # Package
            #

            "installed_packages":
                "rpm -qa",


            #
            # Audit rules
            #

            "audit_rules":
                "cat /etc/audit/audit.rules 2>/dev/null",

        }


        data.update(
            self.execute_commands(
                commands
            )
        )


        return data