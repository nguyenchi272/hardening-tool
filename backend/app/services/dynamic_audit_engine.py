import re

from app.models.finding \
    import Finding

from app.services.rule_loader \
    import load_rules


class DynamicAuditEngine:

    def run(
        self,
        data
    ):

        print(
            "RUNNING DYNAMIC ENGINE"
        )

        findings = []

        rules = load_rules()

        for rule in rules:

            target = \
                rule["check"]["target"]

            content = \
                data.get(
                    target,
                    ""
                )

            check_type = \
                rule["check"]["type"]

            failed = False

            evidence = ""

            #
            # REGEX
            #
            if check_type == "regex":

                pattern = \
                    rule["check"]["pattern"]

                matched = re.search(
                    pattern,
                    content,
                    re.MULTILINE
                )

                if matched:

                    failed = True

                    evidence = \
                        matched.group(0)

            #
            # REGEX NOT MATCH
            #
            elif check_type == "regex_not_match":

                pattern = \
                    rule["check"]["pattern"]

                matched = re.search(
                    pattern,
                    content,
                    re.MULTILINE
                )

                if not matched:

                    failed = True

                    evidence = \
                        "Expected pattern not found"

            #
            # EQUALS
            #
            elif check_type == "equals":

                expected = \
                    rule["check"][
                        "expected_value"
                    ]

                actual = \
                    content.strip()

                if actual != expected:

                    failed = True

                    evidence = \
                        f"Current value: {actual}"

            if failed:

                findings.append(

                    Finding(
                        id=len(findings)+1,

                        finding_id=
                            rule["id"],

                        title=
                            rule["title"],

                        severity=
                            rule["severity"],

                        risk_score=
                            rule["risk_score"],

                        category=
                            rule["category"],

                        description=
                            rule["description"],

                        impact=
                            rule["impact"],

                        evidence=
                            evidence,

                        remediation=
                            rule["remediation"],

                        references=
                            rule["references"],

                        compliance=
                            rule["compliance"],

                        tags=
                            rule["tags"],

                        server=
                            data["hostname"],

                        status="Open"
                    )
                )

        return findings