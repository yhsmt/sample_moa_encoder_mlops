from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct
from cdk import utils, params


def create_s3_bucket(
    construct: Construct, removal_policy=RemovalPolicy.DESTROY
) -> s3.Bucket:
    return s3.Bucket(
        construct,
        utils.name(params.Common.APP_NAME),
        bucket_name=utils.name(params.Common.APP_NAME),
        removal_policy=removal_policy,
    )
