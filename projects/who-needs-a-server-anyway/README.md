# Who-Needs-A-Server-Anyway

Python project demonstrating a serverless REST service using AWS Lambda

## Requirements

1. Your AWS environment was bootstrapped once by an IAM Account with AdministratorAccess policy. If you haven't done so already, run the following command:

```
cdk bootstrap
```

2. Use an IAM account with the necessary permissions. If you do not want to run this project as an administrator, create a new inline policy (e.g. "NonAdminCDKDeploy") as a JSON file with the following content, and assign it to the Lambda developer:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/cdk-*"
            ]
        }
    ]
}
```

## Installation

```
cd ~/projects/who-needs-a-server-anyway
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Usage

**List all AWS CDK stacks**
```
cdk list
```

**Synthesize the CDK app to produce a cloud assembly**
```
cdk synth
```

**Deploy the AWS CDK stack into your AWS environment**
```
cdk deploy
```

**List the deployed lambda functions**
```
aws lambda list-functions
aws lambda list-functions --query 'Functions[].FunctionName' --output text
```

**Try the function URL with curl**
```
# Pattern:
# curl https://<api-id>.execute-api.<region>.amazonaws.com/prod/hello
curl -X GET https://0wcq5gvyqz.execute-api.eu-central-1.amazonaws.com/prod/hello
curl -X GET https://p4mccn5ujk.execute-api.eu-central-1.amazonaws.com/prod/people
```

**Delete the AWS CDK stacks from your AWS environment.**
```
cdk destroy
```
