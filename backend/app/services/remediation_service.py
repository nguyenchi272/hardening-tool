from app.services.ssh_collector \
    import SSHCollector

from app.services.rule_loader \
    import load_rules


class RemediationService:

    def fix_finding(
        self,
        host,
        username,
        password,
        finding_id
    ):

        #
        # Find matching rule
        #
        rules = load_rules()

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
        # No fix block
        #
        if "fix" not in rule:

            raise Exception(
                f"No remediation available"
            )

        #
        # SSH connect
        #
        ssh = SSHCollector(
            host,
            username,
            password
        )

        ssh.connect()

        results = []

        #
        # Execute commands
        #
        for cmd in rule["fix"]:

            output = ssh.run_command(cmd)

            results.append({

                "command": cmd,

                "stdout":
                    output["stdout"],

                "stderr":
                    output["stderr"]
            })

        ssh.close()

        return {

            "status": "success",

            "finding_id":
                finding_id,

            "results":
                results
        }