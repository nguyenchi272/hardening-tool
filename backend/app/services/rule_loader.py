import os
import yaml


RULE_CACHE = []


def load_rules():

    global RULE_CACHE

    #
    # CACHE
    #
    if RULE_CACHE:

        return RULE_CACHE

    rules_dir = "app/rules"

    loaded_rules = []

    #
    # RECURSIVE WALK
    #
    for root, dirs, files in os.walk(
        rules_dir
    ):

        for file in files:

            if not file.endswith(
                ".yaml"
            ):

                continue

            path = os.path.join(
                root,
                file
            )

            with open(
                path,
                "r"
            ) as f:

                rule = yaml.safe_load(f)

                loaded_rules.append(
                    rule
                )

    RULE_CACHE = loaded_rules

    return RULE_CACHE