from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.securescan

def store_scan_result(scan_type, target, result):
    db.scans.insert_one({
        "type": scan_type,
        "target": target,
        "timestamp": datetime.utcnow(),
        "result": result
    })

def get_scan_history():
    return list(db.scans.find().sort("timestamp", -1))
