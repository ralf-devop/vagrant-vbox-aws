$set_environment_variables = <<SCRIPT
tee "/etc/profile.d/awsvars.sh" > "/dev/null" <<EOF
# AWS environment variables
export AWS_DEFAULT_REGION=#{ENV['AWS_DEFAULT_REGION']}
export AWS_ACCESS_KEY_ID=#{ENV['AWS_ACCESS_KEY_ID']}
export AWS_SECRET_ACCESS_KEY=#{ENV['AWS_SECRET_ACCESS_KEY']}
EOF
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-24.04"
  config.vm.box_version = "202510.26.0"

  #config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provision "shell", inline: $set_environment_variables, run: "always"

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "./ansible/playbook.yml"
  end

end
