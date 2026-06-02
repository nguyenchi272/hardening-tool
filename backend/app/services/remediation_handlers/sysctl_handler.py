class SysctlHandler:

    def execute(
        self,
        collector,
        fix_data
    ):

        key = fix_data["key"]

        value = fix_data["value"]

        command = (
            f"sysctl -w {key}={value}"
        )

        result = collector.run_command(

            command,

            sudo=True
        )

        return result