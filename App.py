from flask import Flask, render_template, request
from zap_scan import run_zap_scan
from nmap_scan import run_nmap_scan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    zap_results = nmap_results = None
    if request.method == 'POST':
        target_url = request.form['url']
        zap_results = run_zap_scan(target_url)
        nmap_results = run_nmap_scan(target_url)
    return render_template('index.html', zap=zap_results, nmap=nmap_results)

if __name__ == '__main__':
    app.run(debug=True)
