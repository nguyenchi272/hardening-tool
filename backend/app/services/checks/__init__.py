from app.services.checks \
    import regex_check

from app.services.checks \
    import regex_not_match_check

from app.services.checks \
    import equals_check

from app.services.checks \
    import contains_check

from app.services.checks \
    import not_contains_check

from app.services.checks \
    import service_not_active_check


CHECK_HANDLERS = {

    "regex":
        regex_check.run,

    "regex_not_match":
        regex_not_match_check.run,

    "equals":
        equals_check.run,

    "contains":
        contains_check.run,

    "not_contains":
        not_contains_check.run,

    "service_not_active":
        service_not_active_check.run
}