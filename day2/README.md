# Lab Work Task. Web Server Provisioning
## Review
### Using Ansible v2.3.1 for provisioning nginx + tomcat application stack. 
### Learning by doing.
### Task
###  Create ansible inventory file (name: inventory) with remote host connection details:
###### Remote VM hostname/ip/port
###### Remote ssh login username
###### Connection type
### Develop a playbook (name: site.yml) which is supposed to run against any host (specified in inventory)
#### Develop roles:
###### - java (installs java)
###### - java_test (does only checks that java installed and running properly)
###### - tomcat (installs tomcat)
###### - tomcat_test (does only checks that tomcat installed and running properly)
###### - nginx (installs nginx)
###### - nginx_test (does only checks that nginx installed and running properly)
### Playbook should consist of 2 Plays:
###### - Installation
###### - Verification
## Use handlers to manage tomcat/nginx configuration changes
## Use module debug to check configuration during the installation 
### Define play/roles variables (at least):
###### - tomcat_version
###### - tomcat_home
###### - tomcat_user
###### - tomcat_group
###### - java_version
#### Every task/handler should have a name section with details of task purpose.

#### Software installation requirements:
##### Tomcat AS should be installed from sources (tar.gz) – download from the official site (http://archive.apache.org/dist/tomcat/).
##### Tomcat AS should be owned (and run) by user specified in variable (default: tomcat_as:tomcat_as_group).
##### Tomcat AS version should be 7.x, 8.x (at least 5 versions), exact version to be installed is taken from appropriate variable.
##### Tomcat installation folder (CATALINA_HOME) is /opt/tomcat/$version, where $version is the version of tomcat defined in playbook.
##### Java can be installed from CentOS Repositories
##### Use module yum to install Nginx
##### Use module template for management of nginx cofigs
##### Tomcat home page should be available on port 80 (accessible from Control Machile) via nginx.

#Result:
