# d9scan
###  Python Network Scanner with Backdoor Detection on Network for use on Linux or Windows

d9scan is a script written in Python3 that allows  port scanning, Backdoor Detection on networks.  The program is interactive and simply requires you to run it to begin.  Obtain open ports , asks for option which script you want to run. All scripts are backed by NMAP.


<p align="center" >
<img src="https://pbs.twimg.com/media/E171I5gVIAAG5wa?format=png&name=large" height="350px" width="500px"  alt="d9scan" />
</p>

```
**Usage**

./d9scan~$ python3 scan.py <target>


```



**Scripts**

```bash
>  nmap -v -A scan
>  http-malware-host Detection (recommanded malware detection) 
>  http-dlink-backdoor Detection (dlink backdoor detection)
>  ftp-proftpd-backdoor Detection (ftp proftpd detection runs on port 21)

```

## Requirements
Python3 must be installed on your system in order to function
Install bs4 via pip using `pip install bs4`

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

