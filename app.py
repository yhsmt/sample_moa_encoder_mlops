from aws_cdk import App, Tags

from cdk import (
    stacks,
    utils,
    params,
)


if utils.lack_of_environment_vals():
    raise RuntimeError("lack of environment vals.")

app = App()

stacks = [
    stacks.CdkBaseStack(app, utils.name("cdk-base")),
]

# tags
for stack in stacks:
    for k, v in params.Common.TAGS.items():
        Tags.of(stack).add(k, v)

app.synth()
