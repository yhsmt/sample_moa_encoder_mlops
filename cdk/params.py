import os

from aws_cdk import (
    aws_lambda as lmd,
    aws_logs as logs,
    aws_ec2 as ec2,
    Duration,
)

from cdk import utils


class Common:
    APP_NAME = "sample-moa-encoder-mlops"
    APP_STAGE = os.getenv("CDK_APP_STAGE")
    APP_STAGE_PROD = "prod"
    APP_STAGE_STG = "stg"
    APP_STAGE_IS_PROD = APP_STAGE == APP_STAGE_PROD
    APP_STAGE_IS_STG = APP_STAGE == APP_STAGE_STG
    TAGS = {
        "StackName": utils.name("cdk-base"),
        "Environment": APP_STAGE,
        "Owner": "datalake",
        "Maintainer": "datalake",
    }


class Lambda:
    DEFAULT_MEMORY_SIZE = 128  # MB
    RESERVED_CONCURRENT_EXEC = 10
    RUNTIME = lmd.Runtime.PYTHON_3_12
    ARCHITECTURE = lmd.Architecture.ARM_64
    TIMEOUT_MS = 90000
    LOG_RETENTION = logs.RetentionDays.THREE_MONTHS


class VPC:
    # VPC params to be imported

    if Common.APP_STAGE_IS_PROD:
        # prod
        MAX_AZ = 2
        SUBNET_CIDR_MASK = 24  # ip x 256
    else:
        # nonprod
        MAX_AZ = 2
        SUBNET_CIDR_MASK = 27  # ip x 32


class EC2:
    MACHINE_IMAGE = ec2.MachineImage.latest_amazon_linux2()
    if Common.APP_STAGE_IS_PROD:
        INSTANCE_TYPE = ec2.InstanceType("t3.micro")
    else:
        INSTANCE_TYPE = ec2.InstanceType("t3.micro")


class AppRunner:
    SERVICE_PORT = 80


class S3:
    LIFECYCLE_TTL = Duration.days(1)
    PROD_S3_BUCKET_NAME = "prd-datalake"
    PROD_KMS_KEY_ARN = (
        "arn:aws:kms:*:688022834088:key/2d5a5e8c-b611-4d8e-b87e-b6189127bd4e"
    )
