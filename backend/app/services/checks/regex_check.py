import re


def run(
    content,
    rule
):

    pattern = \
        rule["check"]["pattern"]

    matched = re.search(
        pattern,
        content,
        re.MULTILINE
    )

    if matched:

        return True, matched.group(0)

    return False, ""