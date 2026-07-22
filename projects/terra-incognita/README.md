# Terra-Incognita

A Terraform project that enables the setup of a training environment for a variable number of participants

## Requirements

1. Use an IAM account with the necessary permissions, including the ability to create EC2 instances (for example, using the AdministratorAccess policy)

## Installation

```
cd ~/projects/terra-incognita
terraform init
```

## Usage

**Validate changes**
```
terraform plan
```

**Apply changes**
```
#with default values for variables
terraform apply
#with your own values for variables 
terraform apply -var 'number_trainees=5'
```
Trainer and trainees keys for SSH connection are created in the project folder

**Connect as trainer to the created EC2 instance**
```
ssh -i ./trainer-ssh-key ec2-user@15.183.53.14
```

**Connect as trainee to the created EC2 instance**
```
ssh -i ./training-ssh-key trainee_0@15.183.53.14
```

**Delete previously created resources**
```
#this will also remove the keys for the SSH connection
terraform destroy
```
