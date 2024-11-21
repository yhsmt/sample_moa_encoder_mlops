from aws_cdk import App, Tags

from cdk import (
    stacks,
    utils,
    params,
)


if utils.lack_of_environment_vals():
    raise RuntimeError("lack of environment vals.")

app = App()

storage = stacks.StorageStack(app, utils.name("moa-encoder-storage"))
network = stacks.NetworkStack(app, utils.name("moa-encoder-network"))
training = stacks.TrainingStack(
    app,
    utils.name("moa-encoder-training"),
    bucket=storage.bucket,
    repo=storage.repo,
    vpc=network.vpc,
    private_subnet=network.private_subnet,
)
service = stacks.ServiceStack(app, utils.name("moa-encoder-service"), repo=storage.repo)

# tags
for stack in [storage, training, service]:
    for k, v in params.Common.TAGS.items():
        Tags.of(stack).add(k, v)

app.synth()
