import paramiko


class SSHCollector:

    def __init__(
        self,
        host,
        username,
        password,
        port=22
    ):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        self.client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            timeout=10
        )

    def run_command(
        self,
        command,
        sudo=False
    ):

        if sudo:

            command = (
                f"sudo -S -p '' {command}"
            )

        stdin, stdout, stderr = \
            self.client.exec_command(
                command
            )

        if sudo:

            stdin.write(
                self.password + "\n"
            )

            stdin.flush()

        return {

            "stdout":
                stdout.read().decode(),

            "stderr":
                stderr.read().decode()
        }

    def close(self):
        if self.client:
            self.client.close()