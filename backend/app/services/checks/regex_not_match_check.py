import re

def run(
    content,
    rule
):

    pattern = \
        rule["check"]["pattern"]

    print(
        "RULE =",
        rule["id"]
    )

    print(
        "PATTERN =",
        repr(pattern)
    )

    print(
        "CONTENT =",
        repr(content)
    )

    matched = re.search(
        pattern,
        content,
        re.MULTILINE
    )

    print(
        "MATCHED =",
        matched
    )

    if not matched:

        return (
            True,
            "Expected pattern not found"
        )

    return False, ""