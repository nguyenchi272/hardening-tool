def run(
    content,
    rule
):

    value = \
        rule["check"]["value"]

    if value not in content:

        return (
            True,
            f"Missing: {value}"
        )

    return False, ""