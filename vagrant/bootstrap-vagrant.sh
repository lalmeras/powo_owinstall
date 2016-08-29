#! /bin/bash
set -e

if [ -f /vagrant/vagrant/env.sh ]; then
	. /vagrant/vagrant/env.sh
fi
if [ -d /vagrant/vagrant/certs ]; then
	find /vagrant/vagrant/certs -name "*.pem" -type f -exec cp {} /etc/pki/ca-trust/source/anchors/ \;
	update-ca-trust
fi

if which apt-get &> /dev/null; then
	apt-get update
	apt-get install -y build-essential python-virtualenv python-dev git libssl-dev libffi-dev
fi
if which dnf &> /dev/null; then
	dnf groupinstall ${dnf_trust} --refresh -y -v "Development Tools"
	dnf install ${dnf_trust} --refresh -y -v redhat-rpm-config python-virtualenv python-devel git openssl-devel libffi-devel python2-dnf
fi

venv_path=/opt/powo
mkdir -p $( dirname "$venv_path" )

if [ ! -d "${venv_path}/bin" ]; then
	virtualenv --system-site-packages ${venv_path}
	virtualenv --relocatable ${venv_path}
fi

. "${venv_path}/bin/activate"

# installing dependencies in dist from source
for lib in $( ls /vagrant/vagrant/dist/*/setup.py ); do
	pip install --editable "$( dirname "$lib" )"
done

pip install --editable /vagrant/
powo -v -c /vagrant/vagrant/config/config.yml update
