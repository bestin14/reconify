#!/bin/bash

pd=pwd

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo 'Installing go language'
echo "Y" | apt install golang-go

echo 'installing termcolor module of python'
pip3 install termcolor

echo 'Installing waybackurls'
go install github.com/tomnomnom/waybackurls@latest 

echo 'Installing gau Tool'
go install github.com/lc/gau/v2/cmd/gau@latest

echo 'Installing gospider Tool'
GO111MODULE=on go install github.com/jaeles-project/gospider@latest

echo 'Installing gospider Tool'
git clone https://github.com/xnl-h4ck3r/xnLinkFinder.git
cd xnLinkFinder
python setup.py install
cd $pd

echo 'Installing gospider Tool'
go install github.com/hakluke/hakrawler@latest

echo 'Installing subjs Tool'
GO111MODULE=on go get -u -v github.com/lc/subjs@latest

echo 'Installing JSFinder Tool'
git clone https://github.com/Threezh1/JSFinder.git

echo 'Installing Httpx Tool'
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

echo 'Installation Complete ! you can now run the script '
