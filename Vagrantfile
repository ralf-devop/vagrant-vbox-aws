Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-24.04"
  config.vm.box_version = "202510.26.0"

  #config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "./ansible/playbook.yml"
  end

end
