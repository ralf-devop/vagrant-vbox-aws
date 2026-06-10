#!/bin/bash

# Add SSH keys for authorized user
useradd -m ${user}
mkdir -p /home/${user}/.ssh
echo "${key} ${key_name}" > /home/${user}/.ssh/authorized_keys
chown -R ${user}:${user} /home/${user}/.ssh
chmod 700 /home/${user}/.ssh
chmod 600 /home/${user}/.ssh/authorized_keys
