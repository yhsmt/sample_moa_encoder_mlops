from aws_cdk import aws_ec2 as ec2
from constructs import Construct
from cdk import params, utils


def create_vpc(scope: Construct) -> ec2.Vpc:
    return ec2.Vpc(
        scope,
        "vpc",
        max_azs=params.VPC.MAX_AZ,  # 2つのAZを使用
        nat_gateways=1,  # NAT Gatewayを1つ作成
        subnet_configuration=[
            ec2.SubnetConfiguration(
                name=utils.name(f"{params.Common.APP_NAME}-public"),
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=params.VPC.SUBNET_CIDR_MASK,
            ),
            ec2.SubnetConfiguration(
                name=utils.name(f"{params.Common.APP_NAME}-private-with-egress"),
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                cidr_mask=params.VPC.SUBNET_CIDR_MASK,
            ),
        ],
    )
