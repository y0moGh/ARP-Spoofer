import scapy.all as scapy

# Getting Targets info
def arp_request(ip, ip2):
    
    arp_request = scapy.ARP(pdst=ip)
    arp_request2 = scapy.ARP(pdst=ip2)
    
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    target1_packet = broadcast/arp_request
    target2_packet = broadcast/arp_request2
    
    arp_target1 = scapy.srp(target1_packet, timeout=1, verbose=False)[0]
    arp_target2 = scapy.srp(target2_packet, timeout=1, verbose=False)[0]

    target1 = []
    target2 = []

    for element1 in arp_target1:

        dic1 = {'ip': element1[1].psrc, 'mac': element1[1].hwsrc}
        target1.append(dic1)

    for element2 in arp_target2:
        
        dic2 = {'ip': element2[1].psrc, 'mac': element2[1].hwsrc}
        target2.append(dic2)

    return (target1, target2)
