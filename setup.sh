#!/bin/bash

sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.10 python3.10-venv python3.10-distutils
python3.10 -m venv /home/vagrant/venv
/home/vagrant/venv/bin/pip install -r /vagrant/flask/requirements.txt
