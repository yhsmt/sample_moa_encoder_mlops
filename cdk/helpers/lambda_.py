from aws_cdk import (
    aws_lambda as l,
    Duration,
)
from constructs import Construct
from cdk import utils, params


def create_lambda_function(
    construct: Construct,
    name: str,
    asset_path: str,
    layer: l.LayerVersion,
    env: dict,
    runtime=params.Lambda.RUNTIME,
    architecture=params.Lambda.ARCHITECTURE,
    reserved_concurrent_executions=params.Lambda.RESERVED_CONCURRENT_EXEC,
    timeout=Duration.millis(params.Lambda.TIMEOUT_MS),
    description="",
) -> l.Function:
    return l.Function(
        construct,
        name,
        function_name=utils.name(name),
        code=l.Code.from_asset(path=asset_path),
        layers=[layer],
        handler="function.handler",
        environment=env,
        runtime=runtime,
        architecture=architecture,
        reserved_concurrent_executions=reserved_concurrent_executions,
        timeout=timeout,
        description=description,
    )


def create_lambda_layer(
    construct: Construct, name: str, asset_path: str, description
) -> l.LayerVersion:
    return l.LayerVersion(
        construct,
        name,
        layer_version_name=utils.name(name),
        code=l.Code.from_asset(path=asset_path),
        compatible_architectures=[params.Lambda.ARCHITECTURE],
        compatible_runtimes=[params.Lambda.RUNTIME],
        description=description,
    )
