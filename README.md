# d9scan
###  Python Network Scanner with Backdoor Detection on Network for use on Linux or Windows

d9scan is a script written in Python3 that allows  port scanning, Backdoor Detection on networks.  The program is interactive and simply requires you to run it to begin.  Obtain open ports , asks for option which script you want to run. All scripts are backed by NMAP.

**Scripts**

```bash
>  nmap -v -A scan
>  http-malware-host Detection
>  http-dlink-backdoor Detection
>  ftp-proftpd-backdoor Detection

```

## Requirements
Python3 must be installed on your system in order to function
Pip3 for installation via PyPi repository

## Installation

**Install via Git**

```bash
git clone https://github.com/xadhrit/d9scan.git 
```

```bash
sudo ln -s $(pwd)/scan.py /usr/local/bin/scan
```

## LICENSE
*Distributed under MIT LICENSE*

