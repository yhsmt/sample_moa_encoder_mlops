from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct
from cdk import utils


def create_s3_bucket(
    construct: Construct, name: str, removal_policy=RemovalPolicy.DESTROY
):
    return s3.Bucket(
        construct,
        name,
        bucket_name=utils.name(name),
        removal_policy=removal_policy,
    )
