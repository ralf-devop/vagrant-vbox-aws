# Store-My-Objects

Python project demonstrating how to use Boto3 to store data in an AWS S3 bucket

## Requirements

1. You need an AWS S3 bucket with the prefix "aws-s3-example-bucket". If you haven't done so already, run the following command after replacing "account-id" and selecting your region:

```
aws s3api create-bucket --bucket aws-s3-example-bucket-<account-id>-eu-central-1-an --bucket-namespace account-regional --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1
```

2. Use an IAM account with the necessary permissions. If you do not want to run this project as an administrator, create a new inline policy (e.g. "S3ExampleDevelop") as a JSON file with the following content, and assign it to the Python developer:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AssignARoleActions",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::aws-s3-example-bucket*"
            ]
        },
        {
            "Sid": "AssignARoleActions2",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
```

## Installation

```
cd ~/projects/store-my-objects
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Usage

```
python3 boto_its_your_turn.py
```
