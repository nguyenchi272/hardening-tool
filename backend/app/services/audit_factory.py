from app.services.auditors.rhel_audit \
    import RHELAudit

from app.services.auditors.rocky_audit \
    import RockyAudit

from app.services.auditors.alma_audit \
    import AlmaAudit

from app.services.auditors.oracle_linux_audit \
    import OracleLinuxAudit

from app.services.auditors.ubuntu_audit \
    import UbuntuAudit

from app.services.auditors.debian_audit \
    import DebianAudit


class AuditFactory:

    @staticmethod
    def create(
        os_name,
        ssh
    ):

        mapping = {

            "rhel":
                RHELAudit,

            "rocky":
                RockyAudit,

            "alma":
                AlmaAudit,

            "oracle_linux":
                OracleLinuxAudit,

            "ubuntu":
                UbuntuAudit,

            "debian":
                DebianAudit
        }

        audit_class = mapping.get(
            os_name
        )

        if not audit_class:

            raise Exception(
                f"Unsupported OS: {os_name}"
            )

        return audit_class(
            ssh
        )