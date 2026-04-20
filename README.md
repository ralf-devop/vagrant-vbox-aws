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

### SSH Key Pair
Copy the SSH key pair to the `keys` directory and run the following command on the guest machine to import the public key and enable SSH access to EC2 instances:
```
aws ec2 import-key-pair --key-name myawskey --public-key-material fileb:///home/vagrant/.ssh/aws/aws-key.pub
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
