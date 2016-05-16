# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  # config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.network "private_network", ip: "192.168.55.10"

  # config.vm.network "public_network"

  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = "2"
    vb.memory = "2048"
  end

  config.vm.provision "shell", inline: <<-SHELL
    #sudo apt-get update
    #sudo apt-get install -y apache2
  SHELL

  config.vm.provision "ansible_local" do |ansible|
    #ansible.galaxy_role_file = "galaxy-roles.yml"
    ansible.playbook = "playbook.yml"
    #ansible.verbose = "vvvv"
  end
end
