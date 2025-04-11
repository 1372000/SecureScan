from flask import Flask
from routes.scan_routes import scan_bp
from routes.report_routes import report_bp
from routes.dashboard_routes import dashboard_bp
from auth.routes import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Register blueprints
app.register_blueprint(scan_bp, url_prefix='/api/scan')
app.register_blueprint(report_bp, url_prefix='/api/report')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
