import os
import json
import logging
import boto3


logger = logging.getLogger()
logger.setLevel(logging.INFO)

app_stage = os.environ.get("CDK_APP_STAGE")


def handler(event, context):
    logger.info(f"cdk-base: {app_stage}")
    logger.info(event)
    return {"statusCode": 200, "body": ""}
