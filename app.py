from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Docker Project"

@app.route('/health')
def health():
    return "Application is Healthy"

@app.route('/version')
def version():
    return "Version 2.0"

@app.route('/info')
def info():
    return "Container Project Version 2.0 | Running inside Docker"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
