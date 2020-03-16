#!/usr/bin/env python3
import os
from random import randint


home = os.environ['HOME']


def export(path, data, mode):
    with open(path, mode) as file:
        file.write(data)


def make_dirs():
    os.mkdir(f'{home}/Applications')
    os.mkdir(f'{home}/Scripts')


def netman_conf():
    config = '''[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=false

[device-mac-randomization]
wifi.scan-rand-mac-adress=yes

[connection-mac-randomization]
ethernet.cloned-mac-address=stable
wifi.cloned-mac-address=stable

[ipv6]
ipv6.ip6-privacy=2'''
    export('/etc/NetworkManager/NetworkManager.conf', config, 'w')


def set_hostname():
    host = ''.join(str(randint(0, 9)) for _ in range(10))
    export('/etc/hostname', host, 'w')


def redshift_conf():
    config = '''[redshift]
location-provider=manual

[manual]
lat=47
lon=-122'''
    export(f'{home}/.config/redshift.conf', config, 'w')


def install_apps():
    os.system('curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl')
    os.system('apt install ffmpeg redshift gparted bleachbit')
    os.chdir(f'{home}/Applications/')
    os.system('''version=$(curl -s https://github.com/standardnotes/desktop/releases/latest/ | grep -oE "[0-9]+.[0-9]+.[0-9]+");
                  wget https://github.com/standardnotes/desktop/releases/download/v$version/Standard-Notes-$version.AppImage $$ chmod +x Standard-Notes-$version.AppImage''')
    os.system('''version=$(curl -s https://github.com/bitwarden/desktop/releases/latest/ | grep -oE "[0-9]+.[0-9]+.[0-9]+");
                  wget https://github.com/bitwarden/desktop/releases/download/v$version/Bitwarden-$version-x86_64.AppImage $$ chmod +x Bitwarden-$version-x86_64.AppImage''')
    os.system('''version=$(curl -s https://github.com/keepassxreboot/keepassxc/releases/latest/ | grep -oE "[0-9]+.[0-9]+.[0-9]+");
                  wget https://github.com/keepassxreboot/keepassxc/releases/download/$version/KeePassXC-$version-x86_64.AppImage $$ chmod +x KeePassXC-$version-x86_64.AppImage''')
    os.chdir('/tmp/')
    os.system('''version=$(curl -s https://github.com/atom/atom/releases/latest/ | grep -oE "[0-9]+.[0-9]+.[0-9]+");
                  wget https://github.com/atom/atom/releases/download/v$version/atom-amd64.deb $$ apt install atom-amd64.deb''')


if __name__ == '__main__':
    os.system('apt update && apt -y upgrade')
    set_hostname()
    netman_conf()
    make_dirs()
    install_apps()
    redshit_conf()
