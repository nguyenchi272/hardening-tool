def run(
    content,
    rule
):

    expected = \
        rule["check"][
            "expected_value"
        ]

    actual = content.strip()

    if actual != expected:

        return (
            True,
            f"Current value: {actual}"
        )

    return False, ""