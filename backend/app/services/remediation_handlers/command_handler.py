class CommandHandler:

    def execute(
        self,
        collector,
        fix_data
    ):

        results = []

        commands = fix_data.get(
            "commands",
            []
        )

        for command in commands:

            result = collector.run_command(

                command,

                sudo=True
            )

            results.append({

                "command": command,

                "stdout":
                    result["stdout"],

                "stderr":
                    result["stderr"]
            })

        return results