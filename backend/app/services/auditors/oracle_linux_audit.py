from app.services.auditors.rhel_audit import RHELAudit


class OracleLinuxAudit(RHELAudit):

    def collect(self):

        data = super().collect()

        data.update(
            self.execute_commands({

                "uek_kernel":
                    "uname -r",

                "dnf_automatic":
                    "systemctl is-enabled dnf-automatic"
            })
        )

        return data