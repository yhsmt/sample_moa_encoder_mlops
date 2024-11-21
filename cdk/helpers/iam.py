from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
)


def policy_statement_for_s3_getobject(bucket: s3.Bucket):
    statement = iam.PolicyStatement(effect=iam.Effect.ALLOW)
    statement.add_actions("s3:GetObject")
    statement.add_resources(bucket.bucket_arn + "/*")
    return statement
