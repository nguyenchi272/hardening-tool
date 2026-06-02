from app.services.ssh_collector \
    import SSHCollector

from app.services.rule_loader \
    import load_rules

from app.services.remediation_engine \
    import RemediationEngine

from app.services.os_detector \
    import OSDetector


class RemediationService:

    def fix_finding(
        self,
        host,
        username,
        password,
        finding_id
    ):

        #
        # SSH connect
        #
        ssh = SSHCollector(

            host,

            username,

            password
        )

        ssh.connect()

        try:

            #
            # Detect OS
            #
            os_name = \
                OSDetector.detect(ssh)

            #
            # Load OS-specific rules
            #
            rules = load_rules(
                os_name
            )

            #
            # Find matching rule
            #
            rule = next(
                (
                    r for r in rules
                    if r["id"] == finding_id
                ),
                None
            )

            if not rule:

                raise Exception(
                    f"Rule not found: {finding_id}"
                )

            #
            # No remediation block
            #
            if "fix" not in rule:

                raise Exception(
                    "No remediation available"
                )

            fix_data = rule["fix"]

            #
            # Execute remediation
            #
            engine = RemediationEngine()

            results = engine.execute(

                ssh,

                fix_data
            )

            return {

                "status": "success",

                "finding_id":
                    finding_id,

                "os":
                    os_name,

                "results":
                    results
            }

        finally:

            ssh.close()