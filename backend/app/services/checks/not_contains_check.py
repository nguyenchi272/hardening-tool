def run(
    content,
    rule
):

    value = \
        rule["check"]["value"]

    if value in content:

        return (
            True,
            value
        )

    return False, ""