class BaseAudit:

    def __init__(
        self,
        ssh
    ):
        self.ssh = ssh

    def execute_commands(
        self,
        commands
    ):

        data = {}

        for key, cmd in commands.items():

            try:

                result = \
                    self.ssh.run_command(cmd)

                data[key] = \
                    result["stdout"].strip()

            except Exception as e:

                data[key] = ""

                print(
                    f"[AUDIT ERROR] "
                    f"{key}: {e}"
                )

        return data