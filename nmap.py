from db import store_scan_result
# ...
def run_nmap_scan(host):
    # scan logic...
    result = {proto: nm[host][proto] for proto in nm[host].all_protocols()}
    store_scan_result("nmap", host, result)
    return list(result.keys())
