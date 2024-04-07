import nmap
import socket

def scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='sS')
    for host in nm.all_hosts():
        mac = nm[host].hostname()
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                extrainfo = nm[host][proto][port]['extrainfo']

                return 'Target : %s\nhostname : %s\nProtocol : %s\nport : %s\tstate : %s\tservice : %s\tproduct : %s\tversion : %s\textrainfo : %s' % (host, mac, proto, port, state, service, product, version, extrainfo)


if __name__ == '__main__':
    target = socket.gethostbyname('www.google.com')
    print(scan(target))