#!/usr/bing/env python

#Unfinished version, needs comments

# This program will scan the current network and will return the address and MAC Address

import scapy.all as scapy

# Will create an ARP request directed to broadcast MAC specifying an IP Address.
def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout = 1, verbose = False)[0]

    
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(client_list)

def result_output(results_list):
    print("IP \t\t\tMAC Address\n----------")
    for client in results_list:
        print(client["IP"] + "\t\t" + client["mac"])


# To input IP address
scan_result = scan("0.0.0.1/24")
result_output(scan_result)
