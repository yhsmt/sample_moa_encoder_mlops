from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam,
    Stack,
)
from constructs import Construct
from cdk.helpers import (
    lambda_ as lh,
    iam,
    s3,
)
from cdk import utils


class CdkBaseStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.create_s3_bucket(self, "bucket")

        # main Lambda function
        layer = lh.create_lambda_layer(
            construct=self,
            name="sample-layer",
            asset_path="./lambda/layers/sample_layer",
            description=f"layer for {utils.name('cdk-base-stack')}",
        )

        main_function = lh.create_lambda_function(
            construct=self,
            name="main-function",
            asset_path="./lambda/functions/sample_function",
            layer=layer,
            env={"CDK_APP_STAGE": utils.app_stage()},
            description=f"main function for {utils.name('cdk-base-stack')}",
        )

        main_function.add_to_role_policy(iam.policy_statement_for_s3_getobject(bucket))

