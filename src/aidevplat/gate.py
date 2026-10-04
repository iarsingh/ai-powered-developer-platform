class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("template"): failed.append("template")
    if not body.get("tests_passed"): failed.append("tests")
    return {"passed": not failed, "failed": failed, "applied": False}
