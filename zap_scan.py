import requests
import time

ZAP_API = 'http://zap:8080'  # docker service name
API_KEY = ''  # optional

def run_zap_scan(target):
    scan_url = f'{ZAP_API}/JSON/ascan/action/scan/?apikey={API_KEY}&url={target}'
    requests.get(scan_url)
    time.sleep(5)

    while True:
        status = requests.get(f'{ZAP_API}/JSON/ascan/view/status/').json()['status']
        if status == '100':
            break
        time.sleep(2)

    alerts_url = f'{ZAP_API}/JSON/core/view/alerts/?baseurl={target}'
    alerts = requests.get(alerts_url).json()['alerts']
    return alerts
