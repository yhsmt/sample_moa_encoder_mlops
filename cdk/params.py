import os

from aws_cdk import (
    aws_lambda as lmd,
    aws_logs as logs,
    Duration,
)

from cdk import utils


class Common:
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
        VPC_ID = "vpc-0a35f89ca2decc786"
        VPC_CIDR_BLOCK = "10.58.218.0/23"
        SUBNET_ID = "subnet-03f4fd1e5783edd36"
        AVAILABILITY_ZONE = "ap-northeast-1a"
        SECURITY_GROUP_INBOUND_443_ALLOW = [
            ("100.76.229.0/25", "OpenPaaS"),
            ("100.76.229.128/25", "OpenPaaS"),
            ("100.76.230.0/25", "OpenPaaS"),
        ]
    else:
        # nonprod
        VPC_ID = "vpc-01de5e42aeb17a496"
        VPC_CIDR_BLOCK = "10.58.221.0/24"
        SUBNET_ID = "subnet-0604c623799bc44e6"
        AVAILABILITY_ZONE = "ap-northeast-1a"
        SECURITY_GROUP_INBOUND_443_ALLOW = [
            ("10.58.0.0/16", "ADJ VPN"),
            ("100.76.229.0/25", "OpenPaaS"),
            ("100.76.229.128/25", "OpenPaaS"),
            ("100.76.230.0/25", "OpenPaaS"),
            ("10.96.0.0/16", "preprod"),
            ("10.96.89.4/32", "preprod"),
            ("10.95.79.21/32", "preprod"),
        ]


class S3:
    LIFECYCLE_TTL = Duration.days(1)
    PROD_S3_BUCKET_NAME = "prd-datalake"
    PROD_KMS_KEY_ARN = (
        "arn:aws:kms:*:688022834088:key/2d5a5e8c-b611-4d8e-b87e-b6189127bd4e"
    )
