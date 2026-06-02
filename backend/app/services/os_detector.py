class OSDetector:

    @staticmethod
    def detect(
        collector
    ):

        result = collector.run_command(
            "cat /etc/os-release"
        )

        content = \
            result["stdout"].lower()

        if "ubuntu" in content:
            return "ubuntu"

        if "debian" in content:
            return "debian"

        if "rocky" in content:
            return "rocky"

        if "alma" in content:
            return "alma"

        if "oracle" in content:
            return "oracle_linux"

        if (
            "red hat" in content
            or
            "rhel" in content
        ):
            return "rhel"

        return "unknown"