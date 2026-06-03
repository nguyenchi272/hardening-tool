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

    if not matched:

        return (
            True,
            "Expected pattern not found"
        )

    return False, ""