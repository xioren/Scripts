#!/bin/bash

echo "setting up operating system..."

# updates
sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get autoremove -y
sudo apt-get autoclean -y

# make dires
mkdir ~/Applications

# apt installs
sudo apt-get install ffmpeg curl wget ssh openvpn webp cmatrix mpv  -y

# third party installs
echo "getting third party applications"

# youtube-dl
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

# atom
version=$(curl --silent https://github.com/atom/atom/releases/latest | grep -oP '\d+\.\d+\.\d+')
curl -L https://github.com/atom/atom/releases/download/v${version}/atom-amd64.deb -o ~/Downloads/atom-amd64.deb
sudo dpkg -i ~/Downloads/atom-amd64.deb && rm ~/Downloads/atom-amd64.deb

# bitwarden
version=$(curl --silent https://github.com/bitwarden/desktop/releases/latest | grep -oP '\d+\.\d+\.\d+')
curl -L https://github.com/bitwarden/desktop/releases/download/v${version}/Bitwarden-${version}-amd64.deb -o ~/Downloads/Bitwarden-${version}-amd64.deb
sudo dpkg -i ~/Downloads/Bitwarden-${version}-amd64.deb && rm ~/Downloads/Bitwarden-${version}-amd64.deb

# standard notes
version=$(curl --silent https://github.com/standardnotes/desktop/releases/latest | grep -oP '\d+\.\d+\.\d+')
curl -L https://github.com/standardnotes/desktop/releases/download/v${version}/Standard-Notes-${version}.AppImage -o ~/Applications/Standard-Notes-${version}.AppImage
chmod +x ~/Applications/Standard-Notes-${version}.AppImage

# balena etcher
version=$(curl --silent https://github.com/balena-io/etcher/releases/latest | grep -oP '\d+\.\d+\.\d+')
curl -L https://github.com/balena-io/etcher/releases/download/v${version}/balena-etcher-electron_${version}_amd64.deb -o ~/Downloads/balena-etcher-electron_${version}_amd64.deb
sudo dpkg -i ~/Downloads/balena-etcher-electron_${version}_amd64.deb && rm ~/Downloads/balena-etcher-electron_${version}_amd64.deb

# fix dpkg dependencies
sudo apt-get -f install

# add recent docs removal?

echo "complete....rebooting"

systemctl reboot
