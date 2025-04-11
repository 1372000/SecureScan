import nmap

def run_nmap_scan(host):
    nm = nmap.PortScanner()
    nm.scan(host, '1-1000')
    result = {}
    if host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            result[proto] = nm[host][proto].keys()
    return result
