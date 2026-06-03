from pathlib import Path
import yaml

from app.services.rule_validator \
    import RuleValidator


def load_rules(
    os_name
):

    rules_root = (
        Path(__file__)
        .parent.parent
        / "rules"
    )

    common_path = \
        rules_root / "common"

    os_path = \
        rules_root / os_name

    loaded_rules = []

    search_paths = [
        common_path,
        os_path
    ]

    for path_root in search_paths:

        if not path_root.exists():

            print(
                f"[RULE PATH NOT FOUND] "
                f"{path_root}"
            )

            continue

        for file in path_root.rglob(
            "*.yml"
        ):

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    rule = yaml.safe_load(f)

                RuleValidator.validate(
                    rule
                )

                loaded_rules.append(
                    rule
                )

            except Exception as e:

                print(
                    f"[RULE ERROR] {file}"
                )

                print(str(e))

    return loaded_rules