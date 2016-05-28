# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--nictype1", "virtio"]
    v.memory = 1024
  end

  config.vm.provision :shell do |shell|
    shell.inline = "/vagrant/bootstrap-powo.sh"
    shell.env = { :vagrant_dev => "true" }
  end
end
