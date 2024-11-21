from aws_cdk import (
    aws_s3 as s3,
    aws_ecr as ecr,
    aws_ec2 as ec2,
    Stack,
)
from constructs import Construct
from cdk.helpers import (
    s3 as s3h,
    ecr as ecrh,
    vpc as vpch,
    ec2 as ec2h,
)


class StorageStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.bucket: s3.Bucket = s3h.create_s3_bucket(self)
        self.repo: ecr.Repository = ecrh.create_ecr_repository(self)


class NetworkStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc: ec2.Vpc = vpch.create_vpc(scope=self)
        self.private_subnet: ec2.Subnet = self.vpc.select_subnets(
            subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
        ).subnets[0]


class TrainingStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        bucket: s3.Bucket,
        repo: ecr.Repository,
        vpc: ec2.Vpc,
        private_subnet: ec2.Subnet,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        instance = ec2h.create_instance(
            scope=self,
            vpc=vpc,
            private_subnet=private_subnet,
        )

        bucket.grant_read_write(instance)


class ServiceStack(Stack):
    def __init__(
        self, scope: Construct, id: str, repo: ecr.Repository, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)
