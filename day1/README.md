# Lab Work Task. Tomcat AS Provisioning
## Install Ansible v2.3.1 with python pip. Report details where ansible has been installed.
  <img src="pics/1.jpg">
  <img src="pics/2.jpg">
## Spin up clear CentOS7 VM using vagrant (“vagrant init sbeliakou/centos-7.3-minimal”). Verify connectivity to the host using ssh keys (user: vagrant)
[Vagrantfile](https://github.com/aion3181/Ansible/blob/master/day1/Vagrantfile)
```
  # -*- mode: ruby -*-
  # vi: set ft=ruby :

  # All Vagrant configuration is done below. The "2" in Vagrant.configure
  # configures the configuration version (we support older styles for
  # backwards compatibility). Please don't change it unless you know what
  # you're doing.
  Vagrant.configure("2") do |config|
    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.

    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    config.vm.define "tomcat" do |tomcat|
      tomcat.vm.box = "tomcat"
      tomcat.vm.hostname = 'tomcat'
      tomcat.vm.box_url = "/home/student/cm/ansible/day-1/sbeliakou-vagrant-centos-7.3-x86_64-minimal.box"
      tomcat.vm.network "private_network", ip: "192.168.56.10"

      tomcat.vm.provider :virtualbox do |vb|
      vb.memory = "2048"
      end
  end
  end
```
