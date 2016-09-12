#!/bin/bash -x

# sudo pip3 install virtualenvwrapper

# load virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=/vagrant
export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

# create virtual environment
mkvirtualenv -a $HOME web_scraper
workon web_scraper

# add to .bashrc to automatically enter virtual environment
echo export WORKON_HOME=$HOME/.virtualenvs >> $HOME/.bashrc
echo export PROJECT_HOME=/vagrant >> $HOME/.bashrc
echo export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3' >> $HOME/.bashrc
echo source /usr/local/bin/virtualenvwrapper.sh >> $HOME/.bashrc
echo workon web_scraper >> $HOME/.bashrc

pip3 install beautifulsoup

# Set default directory to Django project folder
echo cd /vagrant/ >> $HOME/.bashrc
