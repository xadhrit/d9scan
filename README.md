# d9scan
### Multi-threaded Python Port Scanner with Backdoor Detection on Network for use on Linux or Windows

d9scan is a script written in Python3 that allows multi-threaded port scanning, Backdoor Detection on networks.  The program is interactive and simply requires you to run it to begin.  Once started, you will be asked to input an IP address or a FQDN as d9scan does resolve hostnames. Obtain open ports , asks for option which script you want to run. All scripts are backed by NMAP.

## Requirements
Python3 must be installed on your system in order to function
Pip3 for installation via PyPi repository

## Installation
**Installation via Pip**

```bash 
pip3 install d9scan
```

Run by typing:
```bash
d9scan
```

**Install via Git**

```bash
git clone https://github.com/xadhrit/d9scan.git #to save the program to your machine, or utilize the download option
```

You can add Threader3000 to run from any directory by adding a symbolic link:

```bash
sudo ln -s $(pwd)/scan.py /usr/local/bin/scan
```

## LICENSE
*This tool is under a free license for use, however it is up to the user to observe all applicable laws and appropriate uses for this tool.  The creator does not condone, support, suggest, or otherwise promote unethical or illegal behavior.  You use this tool at your own risk, and under the assumption that you are utilizing it against targets and infrastructure to which you have permission to do so.  Any use otherwise is at your peril and against the terms of use for the tool.*

