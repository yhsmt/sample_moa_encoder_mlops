from aws_cdk import (
    aws_ecr as ecr,
)
from constructs import Construct
import aws_cdk.aws_apprunner_alpha as apprunner
from cdk import params


def create_apprunner_service(
    scope: Construct,
    repo: ecr.Repository,
) -> apprunner.Service:
    apprunner.Service(
        scope=scope,
        id="Service",
        source=apprunner.Source.from_ecr(
            image_configuration=apprunner.ImageConfiguration(
                port=params.AppRunner.SERVICE_PORT
            ),
            repository=repo,
            tag_or_digest="latest",
        ),
    )
