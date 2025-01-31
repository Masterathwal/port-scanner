import socket 

def scan(target, ports):

    print('\n' + 'Starting Scan for IP Address: ' + str(target))

    for port in range(1,ports):
        portscan(target, port); 

def portscan(ipaddress,port):

    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print("[+] Port Opened " + str(port))
        sock.close()

    except:
        pass

targets = input("[*] Enter IP Addresses of the Targets (split them by ,): ")
ports = int(input("[*] How many Ports to Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")

    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)

else:
    scan(targets,ports)