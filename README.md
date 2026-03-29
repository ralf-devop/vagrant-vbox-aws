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
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

Changes to these variables are applied to the guest machine after the first up, an up after a halt, or an up/resume after a suspend.

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
