from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def index():
    return """<!doctype html><html><head><title>University Result Portal</title></head>
    <body><h1>University Result Portal</h1><p>Semester results service is operational.</p></body></html>"""

@app.get("/health")
def health():
    return jsonify(status="ok", service="result-portal")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
