import os
import re

APP_STAGE_PRODUCTION = "prod"
APP_STAGE_STAGING = "stg"


def lack_of_environment_vals():
    app_stage = os.getenv("CDK_APP_STAGE")
    if app_stage is None:
        return True
    is_dev = re.match(r"dev-", app_stage)
    if app_stage in ["prod", "stg"] or is_dev:
        if (
            os.getenv("CDK_DEFAULT_ACCOUNT") is not None
            and os.getenv("CDK_DEFAULT_REGION") is not None
        ):
            return False
        else:
            return True
    else:
        return True


def name(trunk: str, delimiter: str = "-"):
    app_stage = os.getenv("CDK_APP_STAGE")
    return f"{app_stage.replace('-', delimiter)}{delimiter}{trunk}"


def app_stage():
    return os.getenv("CDK_APP_STAGE")
