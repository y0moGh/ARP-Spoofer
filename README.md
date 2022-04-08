![img](https://img.shields.io/badge/-python%203.9-blue) ![img](https://img.shields.io/badge/-Debian-yellowgreen)

# ARP-Spoofer

Fast & useful arp-spoofer. You only have to run it once (not like others)

<h3 text align="center"> Modules </h3>

```py
import argparse, re, subprocess
import scapy.all as scapy
from ARPR import *
```
<h3 text align="center"> Usage </h3>

<h4> You must be root </h4> 

```yml
> sudo python arp-spoofer.py --help

usage: arp-spoofer.py [-h] [-i INTERFACE] [-t IP] [-s SIP]

optional arguments:
  -h, --help | show this help message and exit   
  -i INTERFACE, --interface INTERFACE | Interfece which you want to use   
  -t IP, --target IP | Target ip you want to spoof       
  -s SIP, --supplant SIP | Ip you want to impersonate 
```
