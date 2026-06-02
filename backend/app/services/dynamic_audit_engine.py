from app.models.finding \
    import Finding

from app.services.rule_loader \
    import load_rules

from app.services.checks \
    import CHECK_HANDLERS


class DynamicAuditEngine:

    def run(
        self,
        os_name,
        data
    ):

        findings = []

        rules = load_rules(
            os_name
        )

        for rule in rules:

            try:

                check_type = \
                    rule["check"]["type"]

                handler = \
                    CHECK_HANDLERS.get(
                        check_type
                    )

                if not handler:

                    print(
                        f"Unknown check type: {check_type}"
                    )

                    continue

                target = \
                    rule["check"]["target"]
                
                print(
                    "AVAILABLE KEYS:"
                )

                print(
                    list(data.keys())
                )

                print(
                    "LOOKING FOR:",
                    target
                )

                content = \
                    data.get(
                        target,
                        ""
                    )

                failed, evidence = \
                    handler(
                        content,
                        rule
                    )

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

                            server=data.get(
                                "hostname",
                                "unknown"
                            ),

                            host=data["host"],

                            status="Open"
                        )
                    )

            except Exception as e:

                print(
                    f"Rule failed: {rule.get('id')}"
                )

                print(str(e))

        return findings