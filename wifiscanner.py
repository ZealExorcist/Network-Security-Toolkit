import scapy.all as scapy
import re
import socket

def wifi(ip_add_range_entered):

    arp_result = scapy.arping(ip_add_range_entered, verbose=False)[0]

    for sent, received in arp_result:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
        except socket.herror:
            hostname = "Unknown"

        return f"IP: {ip} MAC: {mac} Hostname: {hostname}"
