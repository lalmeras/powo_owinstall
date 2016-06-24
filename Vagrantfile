# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.define "ubuntu_trusty" do |ubuntu_trusty|
    ubuntu_trusty.vm.box = "ubuntu/trusty64"
  end
  config.vm.define "fedora_23" do |fedora_23|
    fedora_23.vm.box = "fedora/23-cloud-base"
  end

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--nictype1", "virtio"]
    v.memory = 1024
  end

  config.vm.provision :shell do |shell|
    shell.inline = "/vagrant/bootstrap-powo.sh"
    shell.env = { :vagrant_dev => "true" }
  end
end
