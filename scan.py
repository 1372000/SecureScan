import time
import json
import requests

ZAP_API = 'http://localhost:8080'  # Assuming ZAP is running with API enabled
API_KEY = ''  # If ZAP has an API key set

def run_zap_scan(target):
    scan_url = f'{ZAP_API}/JSON/ascan/action/scan/?apikey={API_KEY}&url={target}'
    requests.get(scan_url)
    time.sleep(5)

    status_url = f'{ZAP_API}/JSON/ascan/view/status/?apikey={API_KEY}'
    while True:
        status = requests.get(status_url).json()['status']
        if status == '100':
            break
        time.sleep(2)

    report_url = f'{ZAP_API}/JSON/core/view/alerts/?apikey={API_KEY}&baseurl={target}'
    alerts = requests.get(report_url).json()['alerts']
    return alerts
