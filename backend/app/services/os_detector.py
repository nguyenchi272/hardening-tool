from app.utils.os_parser import parse_os_name


class OSDetector:

    @staticmethod
    def detect(collector):

        result = collector.run_command(
            "cat /etc/os-release"
        )

        return parse_os_name(
            result["stdout"]
        )