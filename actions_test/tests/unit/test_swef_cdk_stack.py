import aws_cdk as core
import aws_cdk.assertions as assertions

from swef_cdk.swef_cdk_stack import SwefCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in swef_cdk/swef_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SwefCdkStack(app, "swef-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
