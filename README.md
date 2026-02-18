# Vagrant-Vbox-AWS

My vagrant vbox environment to manage Amazon Web Services.

## Required Software

 * [Vagrant](https://developer.hashicorp.com/vagrant/install)
 * [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Provison with Ansible

The configuration is defined as an ansible playbook.
Changes in a running environment can be applied as follows:
`ansible-playbook --connection=local --inventory 127.0.0.1, /vagrant/ansible/playbook.yml`
