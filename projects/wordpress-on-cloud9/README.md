# Wordpress-On-Cloud

A CloudFormation template project that creates a resource stack for WordPress

## Requirements

1. Use an IAM account with the necessary permissions, including the ability to create EC2 instances (for example, using the AdministratorAccess policy)

2. Connecting to port 3306 is permitted in accordance with your security groups. If you haven't done so already, substitute your group-id and run the following command:
```
aws ec2 authorize-security-group-ingress --group-id sg-0678298e6e8939z27 --protocol tcp --port 3306 --cidr 0.0.0.0/0
```

## Installation

```
# Change to the project directory
cd ~/projects/wordpress-on-cloud9
# Validate template
aws cloudformation validate-template --template-body file://wordpress.yaml
# Apply template to create stack, substitute the value for AdminPassParameter
aws cloudformation create-stack --stack-name WordPressStack --template-body file://wordpress.yaml --parameters ParameterKey=AdminPassParameter,ParameterValue=mySecretPass
# Check stack status
aws cloudformation describe-stacks --stack-name WordPressStack
```

## Usage

**Get database hostname**
```
aws rds describe-db-instances --output text --db-instance-identifier mysql4wordpress --query 'DBInstances[*].Endpoint.Address'
```

**Create WordPress database**
```
# Get cert for ssl protected mysql connection
curl -o global-bundle.pem https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
# Connect to database
mysql -h wordpressstack-rdsinstance-htkjzzwkamo7.r79mskk6ou0q.eu-central-1.rds.amazonaws.com -P 3306 -u wordpress_admin -p --ssl-mode=VERIFY_IDENTITY --ssl-ca=./global-bundle.pem
# Create database
mysql> CREATE DATABASE wordpress;
mysql> SHOW DATABASES;
mysql> quit
```

**Get webserver ip address**
```
aws ec2 describe-instances --output text --query 'Reservations[*].Instances[*].PublicIpAddress'
```

**Use these Urls to configure WordPress via a web browser**

```
# Use the IP address from the previous step
http://18.122.61.129/wp-admin/
http://18.122.61.129/wp-login.php
http://18.122.61.129/phpinfo.php
```

## Uninstallation

```
# Change to the project directory
cd ~/projects/wordpress-on-cloud9
# Delete Stack
aws cloudformation delete-stack --stack-name WordPressStack
```
