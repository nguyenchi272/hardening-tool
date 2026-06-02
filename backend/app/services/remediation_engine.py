class RemediationEngine:

    def execute(
        self,
        ssh,
        fix_data
    ):

        if not fix_data.get(
            "supported",
            False
        ):

            raise Exception(
                "Remediation not supported"
            )

        commands = \
            fix_data.get(
                "commands",
                []
            )

        if not commands:

            raise Exception(
                "No remediation commands defined"
            )

        results = []

        for cmd in commands:

            output = ssh.run_command(
                cmd,
                sudo=True
            )

            results.append({

                "command": cmd,

                "stdout":
                    output["stdout"],

                "stderr":
                    output["stderr"]
            })

        return {

            "safe":
                fix_data.get(
                    "safe",
                    False
                ),

            "requires_restart":
                fix_data.get(
                    "requires_restart",
                    False
                ),

            "requires_reboot":
                fix_data.get(
                    "requires_reboot",
                    False
                ),

            "manual_review":
                fix_data.get(
                    "manual_review",
                    False
                ),

            "results":
                results
        }