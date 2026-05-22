import re


def parse_os_name(os_release: str):

    #
    # PRETTY_NAME="Red Hat Enterprise Linux 9.4 (Plow)"
    #
    pretty_match = re.search(
        r'PRETTY_NAME="(.+?)"',
        os_release
    )

    if pretty_match:

        return pretty_match.group(1)

    #
    # NAME="Oracle Linux Server"
    #
    name_match = re.search(
        r'NAME="(.+?)"',
        os_release
    )

    if name_match:

        return name_match.group(1)

    return "Unknown Linux"