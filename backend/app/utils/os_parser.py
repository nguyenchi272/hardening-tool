import re


def parse_os_name(os_release: str):

    content = os_release.lower()


    # RHEL
    if "red hat enterprise linux" in content:
        return "rhel"


    # Rocky
    if "rocky linux" in content:
        return "rocky"


    # Alma
    if "alma linux" in content:
        return "alma"


    # Oracle Linux
    if (
        "oracle linux" in content
        or "oracle linux server" in content
    ):
        return "oracle_linux"


    # Ubuntu
    if "ubuntu" in content:
        return "ubuntu"


    # Debian
    if "debian" in content:
        return "debian"


    # CentOS (nếu sau này thêm)
    if "centos" in content:
        return "centos"


    return "unknown"