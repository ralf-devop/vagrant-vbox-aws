# Vagrant-Vbox-AWS

My vagrant vbox environment to manage Amazon Web Services.

## Required Software

 * [Vagrant](https://developer.hashicorp.com/vagrant/install)
 * [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Provison with Ansible

The configuration is defined as an ansible playbook.
Changes in a running environment can be applied as follows:
```
ansible-playbook --connection=local --inventory 127.0.0.1, /vagrant/ansible/playbook.yml
```

## Configuration
### Environment variables
The following host variables are passed on to the guest machine:

* `AWS_DEFAULT_REGION`
* `AWS_DEFAULT_OUTPUT`
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

Changes to these variables are applied to the guest machine after the first up, an up after a halt, or an up/resume after a suspend.

**Example:**
```
export AWS_DEFAULT_REGION=eu-central-1
export AWS_DEFAULT_OUTPUT=json
export AWS_ACCESS_KEY_ID=HGTE7FEWSC8JIKWQTVEP
export AWS_SECRET_ACCESS_KEY=3tH6+jweTB78+QwcMK28GvnaPJR+31fUsWQYChU4
```
## AWS CLI - EC2

### SSH Key Pair
Copy the SSH key pair to the `keys` directory and run the following command on the guest machine to import the public key for later SSH access to EC2 instances:
```
aws ec2 import-key-pair --key-name myawskey --public-key-material fileb:///home/vagrant/.ssh/aws/aws-key.pub
```

### Frist Steps

**Get Key Name**
```
aws ec2 describe-key-pairs --output text --query 'KeyPairs[*].KeyName'
```
**Get description for all instances**
```
aws ec2 describe-instances
```
**Run new instance**  
Select an AMI from the catalog that is available for your AWS region, and choose the instance type.
```
aws ec2 run-instances --image-id ami-0de6934e87badb694 --instance-type t2.micro --key-name myawskey
```
**Get InstanceId**
```
aws ec2 describe-instances --output text --query 'Reservations[*].Instances[*].InstanceId'
```
**Get Security GroupId**
```
aws ec2 describe-instances --output text --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId'
```
**Open port 22 for ssh connection**
```
aws ec2 authorize-security-group-ingress --group-id sg-0678298e6e8939z27 --protocol tcp --port 22 --cidr 0.0.0.0/0
```
**Get Public IP Address**
```
aws ec2 describe-instances --output text --query 'Reservations[*].Instances[*].PublicIpAddress'
```
**Establish ssh connection**
```
ssh -i ~/.ssh/aws/aws-key ec2-user@18.123.63.317
```
**Stop instance**  
Stopped instances do not incur any costs!
```
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```
**(Re)Start instance**
```
aws ec2 start-instances --instance-ids i-1234567890abcdef0
```
**Terminate instance**  
Irreversible!
```
aws ec2 terminate-instance --instance-ids i-1234567890abcdef0 --skip-os-shutdown
```

## AWS CDK
### Python
Here are the commands to get started with a Python project:
```
mkdir <project>
cd <project>
cdk init sample-app --language python
source .venv/bin/activate
python -m pip install -r requirements.txt
```
