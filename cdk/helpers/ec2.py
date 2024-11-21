from aws_cdk import aws_ec2 as ec2, CfnOutput
from constructs import Construct
from cdk import params, utils


def create_instance(
    scope: Construct, vpc: ec2.Vpc, private_subnet: ec2.Subnet
) -> ec2.Vpc:
    key_pair = ec2.KeyPair(
        scope,
        "key-pair",
        format=ec2.KeyPairFormat.PPK,
        key_pair_name=utils.name(f"{params.Common.APP_NAME}-training-ec2"),
    )
    instance = ec2.Instance(
        scope,
        "instance",
        vpc=vpc,
        vpc_subnets=ec2.SubnetSelection(
            subnets=[private_subnet]
        ),  # 特定の Private Subnet を指定
        instance_type=params.EC2.INSTANCE_TYPE,  # インスタンスタイプ
        machine_image=params.EC2.MACHINE_IMAGE,
        key_pair=key_pair,  # SSH 用のキーペア名を指定
    )

    # インスタンスの ID を出力
    CfnOutput(scope, "TrainingInstanceID", value=instance.instance_id)

    return instance
