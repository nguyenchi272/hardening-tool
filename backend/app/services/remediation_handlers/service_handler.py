class ServiceHandler:

    def execute(
        self,
        collector,
        fix_data
    ):

        service = fix_data["service"]

        action = fix_data["action"]

        command = (
            f"systemctl {action} {service}"
        )

        return collector.run_command(

            command,

            sudo=True
        )