from flask import Blueprint, request, jsonify
from scanners.zap_scan import run_zap_scan
from scanners.nmap_scan import run_nmap_scan
from database.db import db

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/', methods=['POST'])
def run_scan():
    data = request.get_json()
    target = data.get('target')
    zap_result = run_zap_scan(target)
    nmap_result = run_nmap_scan(target)
    
    scan_record = {
        'target': target,
        'zap': zap_result,
        'nmap': nmap_result
    }
    db.scans.insert_one(scan_record)
    return jsonify(scan_record), 200
