from aws_cdk import aws_ecr as ecr, RemovalPolicy
from constructs import Construct
from cdk import utils, params


def create_ecr_repository(construct: Construct) -> ecr.Repository:
    return ecr.Repository(
        scope=construct,
        id="ecr-repo",
        repository_name=utils.name(params.Common.APP_NAME),
    )
