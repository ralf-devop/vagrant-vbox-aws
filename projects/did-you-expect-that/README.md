# Did-You-Expect-That

A Python project that demonstrates how to use Testinfra to check a server’s status

## Requirements

1. The EC2 instance to be tested is running.

2. You are logged in with an account that is authorised to connect to the EC2 instance under test.

## Installation

```
cd ~/projects/did-you-expect-that
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Usage

**Optional: Passphrase for EC2 SSH access key**

If you are using an EC2 SSH access key with a passphrase, you can avoid having to enter the passphrase multiple times during the test run by using ssh-add:
```
# Start ssh-agent if not started
eval "$(ssh-agent -s)"
# Add your private key
ssh-add /home/vagrant/.ssh/aws/aws-key
# Check if the key is added
ssh-add -l
```

**Test execution**
```
pytest -v --ssh-identity-file=~/.ssh/aws/aws-key --hosts='ssh://ec2-user@18.123.63.317'
```
