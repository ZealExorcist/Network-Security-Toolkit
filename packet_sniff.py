<<<<<<< HEAD
from scapy.all import *

def packet(count):
    pack = ""
    packets = sniff(count = count)
    for packet in packets:
        pack += str(packet) + "\n"
    return pack

if __name__ == "__main__":
=======
from scapy.all import *

def packet(count):
    pack = ""
    packets = sniff(count = count)
    for packet in packets:
        pack += str(packet) + "\n"
    return pack

if __name__ == "__main__":
>>>>>>> 97e50f3017aeaf17bbac80f8a53421e8c5629711
    print(packet(5))