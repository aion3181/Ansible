# Ansible
# Lab Work Task. Web Server Provisioning
## Review
## Developing custom modules and filters. Learning by doing.
## Task
### On Host Node (Control Machine):
###  Develop custom filter to select an url to download mongodb depends on OS name and S/W version from https://www.mongodb.org/dl/linux/
### Requirements:
### - Write a playbook (name: mongodb.yml) to prove that this module works
### - At least 9 versions of MongoDB for 3 different Linux distributives (list with links)
### - Filter should process a list of urls and takes 3 options: os_family (discovered by ansible, variable, produced by setup module), os release number and mongodb_version (set in play vars)
### See example in Appendix A

###  Develop custom module to manage VirtualBox:
### Arguments: 
###  path to vagrantfile
###  state: started, stopped, destroyed
### Return values:
###  state: running, stopped, not created
### - ip address, port
### - path to ssh key file
### - username to connect to VM
### - os_name
### - RAM size
### Errors:
### - file doesn’t exists
### - failed on creation
### - etc

###  Create a playbook (name: stack.yml) to provision Tomcat stack (nginx + tomcat) on VirtualBox VM
### Requirements:
### - 2 Plays: provision VM, roll out Tomcat stack (using roles from previous lab work)
### - 2nd play should work with dynamically composed Inventory (connection settings to VM), http://docs.ansible.com/ansible/add_host_module.html

###  Verification Procedure: playbook will be checked by instructor’s CI system as follows:
### 5.1 Connect to student’s host by ssh
### 5.2 Go into the folder ...
### 5.3 Destroy: vagrant destroy
### 5.4 Execute VM provisioning: ansible-playbook stack.yml -i localhost, -c local -vv 
### 5.5 If previous steps are done successfully, instructor will check report (pdf-file)
###  Feedback: report issues/problems you had during the development of playbook and time spent for development.
