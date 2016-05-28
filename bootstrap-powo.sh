#! /bin/bash

set -e

pushd /vagrant
if [ -f env.sh ]; then
	. env.sh
fi
popd

powo_path="/usr/local/powo"
etc_path="/etc/powo"
playbooks_path="${etc_path}/playbooks"
roles_path="${powo_path}/roles"
dependencies_path="${powo_path}/ansible-dependencies"
virtualenv_path="${powo_path}/virtualenv"

mkdir -p ${powo_path}
mkdir -p ${virtualenv_path}
mkdir -p ${dependencies_path}

apt-get update
apt-get install -y python-virtualenv python-dev git libssl-dev libffi-dev

if [ ! -d "${virtualenv_path}/bin" ]; then
	virtualenv --system-site-packages ${virtualenv_path}
fi

. ${virtualenv_path}/bin/activate
pip install --upgrade pip
pip install --upgrade ansible
export PATH=$PATH:${virtualenv_path}/bin

mkdir /var/log/powo

if [ "${vagrant_dev?false}" != "false" ]; then
	ln -s /vagrant/etc ${etc_path}
	ln -s /vagrant/playbooks ${playbooks_path}
	ln -s /vagrant/roles ${roles_path}
else
	echo TODO
fi

# during /home move, cwd must not be /home
cd /root
ansible-galaxy install $( [ "${always_trust_ssl}" == "true" ] && echo "--ignore-certs" ) \
				-r ${etc_path}/requirements.yml -p ${dependencies_path}
ANSIBLE_CONFIG="${etc_path}/ansible.cfg" ansible-playbook ${playbooks_path}/playbook.yml
