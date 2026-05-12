from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)


class WhoNeedsAServerAnywayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function resource
        hello_world_function = _lambda.Function(
            self,
            "HelloWorldFunction",
            runtime = _lambda.Runtime.NODEJS_20_X, # Choose any supported Node.js runtime
            code = _lambda.Code.from_asset("lambda"), # Points to the lambda directory
            handler = "hello.handler", # Points to the 'hello' file in the lambda directory
        )

        # Define the API Gateway resource
        api = apigateway.LambdaRestApi(
            self,
            "HelloWorldApi",
            handler = hello_world_function,
            proxy = False,
        )

        # Define the '/hello' resource with a GET method
        hello_resource = api.root.add_resource("hello")
        hello_resource.add_method("GET")

        # Define the Lambda function resource
        get_people_function = _lambda.Function(
            self,
            "GetPeopleFunction",
            runtime = _lambda.Runtime.NODEJS_20_X, # Choose any supported Node.js runtime
            code = _lambda.Code.from_asset("lambda"), # Points to the lambda directory
            handler = "people.handler", # Points to the 'people' file in the lambda directory
        )

        # Define the API Gateway resource
        api = apigateway.LambdaRestApi(
            self,
            "GetPeopleApi",
            handler = get_people_function,
            proxy = False,
        )

        # Define the '/people' resource with a GET method
        people_resource = api.root.add_resource("people")
        people_resource.add_method("GET")
