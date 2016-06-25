#! /bin/bash

set -e

if [ -f /vagrant/env.sh ]; then
	. /vagrant/env.sh
fi

powo_path="/usr/local/powo"
etc_path="/etc/powo"
playbooks_path="/etc/powo-playbooks"
roles_path="${powo_path}/roles"
dependencies_path="${powo_path}/ansible-dependencies"
virtualenv_path="${powo_path}/virtualenv"

mkdir -p ${powo_path}
mkdir -p ${virtualenv_path}
mkdir -p ${dependencies_path}

if which apt-get &> /dev/null; then
	apt-get update
	apt-get install -y python-virtualenv python-dev git libssl-dev libffi-dev
fi
if which dnf &> /dev/null; then
	dnf groupinstall ${dnf_trust} --refresh -y -v "Development Tools"
	dnf install ${dnf_trust} --refresh -y -v redhat-rpm-config python-virtualenv python-devel git openssl-devel libffi-devel python2-dnf
fi

if [ ! -d "${virtualenv_path}/bin" ]; then
	virtualenv --system-site-packages ${virtualenv_path}
fi

. ${virtualenv_path}/bin/activate
pip install --upgrade pip
pip install --upgrade ansible
export PATH=$PATH:${virtualenv_path}/bin

mkdir -p /var/log/powo

if [ "${vagrant_dev:-false}" == "false" ]; then
	echo "powo repository cloned in /root"
	base_path=/root/powo
	if [ ! -d "$base_path" ]; then
		git clone https://github.com/openwide-java/powo.git $base_path
	fi
	git -C $base_path pull
	if [ -f /vagrant/playbooks/vars/env.yml ]; then
		cp /vagrant/playbooks/vars/env.yml $base_path/playbooks/vars/env.yml
	elif [ -f ./env.yml ]; then
		cp env.yml "$base_path/playbooks/vars/env.yml"
	fi
else
	base_path=/vagrant
	if which dnf &> /dev/null; then
		echo sslverify=False >> /etc/dnf/dnf.conf
	fi
fi

ln -sf -T ${base_path}/etc ${etc_path}
ln -sf -T ${base_path}/playbooks ${playbooks_path}
ln -sf -T ${base_path}/roles ${roles_path}

# during /home move, cwd must not be /home
cd /root
ansible-galaxy install $( [ "${always_trust_ssl}" == "true" ] && echo "--ignore-certs" ) \
				-r ${etc_path}/requirements.yml -p ${dependencies_path}
ANSIBLE_CONFIG="${etc_path}/ansible.cfg" ansible-playbook ${playbooks_path}/playbook.yml
