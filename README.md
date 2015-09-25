# YouTube-Downloader
Implementing the youtube-dl API

1. Install YouTube-DL in RHEL/CentOS and Fedora

The youtube-dl program can be installed by enabling epel repository under your systems. Once enabled, you can install using ‘yum‘ package manager tool as shown.
# yum install youtube-dl

If you don’t wish to add any third party repository, you can still install it right away using curl or wget command as shown.

# curl https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
OR
# wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

Your system must have curl or wget packages installed to fetch the recent version youtube-dl file. If you don’t have them, you may yum to get it.

After fetching the file, you need to set a executable permission on the script to execute properly.

chmod a+rx /usr/local/bin/youtube-dl





2. Install YouTube-DL in Ubuntu/Linux Mint and Debian

Ubuntu users can download and install latest youtube-dl version from the webupd8 PPA as shown.

$ sudo add-apt-repository ppa:nilarimogard/webupd8
$ sudo apt-get update
$ sudo apt-get install youtube-dl

Similarly, instead using any third party PPA, you can use curl or wget command to install latest version of youtube-dl script as shown.

$ sudo curl https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
OR
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

After downloading the script, set the executable permission.

$ sudo chmod a+rx /usr/local/bin/youtube-dl



3. OS X users can install youtube-dl with Homebrew.

brew install youtube-dl

You can also use pip:

sudo pip install youtube-dl




Update YouTube-DL

Youtube-dl itself can be updated to the latest version using the following command.

# youtube-dl -U

