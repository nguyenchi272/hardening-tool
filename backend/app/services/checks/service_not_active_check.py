def run(
    content,
    rule
):

    if content.strip() != "active":

        return (
            True,
            f"Service status: {content}"
        )

    return False, ""