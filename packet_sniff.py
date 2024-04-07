from scapy.all import *
import socket

def packet(count):
    pack = ""
    packets = sniff(count = count)
    for packet in packets:
        pack += str(packet) + "\n"
    return pack

if __name__ == "__main__":
    print(packet(5))