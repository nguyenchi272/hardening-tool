import re


REQUIRED_FIELDS = [

    "id",
    "title",
    "severity",
    "risk_score",
    "category",
    "description",
    "impact",
    "check",
    "remediation"
]


VALID_SEVERITIES = [

    "Critical",
    "High",
    "Medium",
    "Low",
    "Info"
]


VALID_CHECK_TYPES = [

    "regex",
    "regex_not_match",
    "equals",
    "contains",
    "not_contains",
    "service_not_active"
]


class RuleValidator:

    @staticmethod
    def validate(rule):

        #
        # REQUIRED FIELDS
        #
        for field in REQUIRED_FIELDS:

            if field not in rule:

                raise Exception(
                    f"Missing field: {field}"
                )

        #
        # SEVERITY
        #
        severity = rule["severity"]

        if severity not in VALID_SEVERITIES:

            raise Exception(
                f"Invalid severity: {severity}"
            )

        #
        # RISK SCORE
        #
        risk_score = rule["risk_score"]

        if not isinstance(
            risk_score,
            int
        ):

            raise Exception(
                "risk_score must be integer"
            )

        if risk_score < 0 or risk_score > 10:

            raise Exception(
                "risk_score must be 0-10"
            )

        #
        # CHECK
        #
        check = rule["check"]

        if "type" not in check:

            raise Exception(
                "check.type missing"
            )

        if "target" not in check:

            raise Exception(
                "check.target missing"
            )

        check_type = check["type"]

        if check_type not in VALID_CHECK_TYPES:

            raise Exception(
                f"Invalid check type: {check_type}"
            )

        #
        # REGEX VALIDATION
        #
        if check_type in [

            "regex",
            "regex_not_match"
        ]:

            pattern = check.get(
                "pattern"
            )

            if not pattern:

                raise Exception(
                    "Regex pattern missing"
                )

            try:

                re.compile(pattern)

            except Exception:

                raise Exception(
                    f"Invalid regex: {pattern}"
                )

        return True