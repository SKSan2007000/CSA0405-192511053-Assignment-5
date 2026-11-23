#!/usr/bin/env python3
"""Start a local sample portal and optionally run ApacheBench against it."""
import argparse, subprocess, threading, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b'University Result Portal - benchmark response\n'
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args): pass

parser = argparse.ArgumentParser()
parser.add_argument('--requests', type=int, default=1000)
parser.add_argument('--concurrency', type=int, default=20)
args = parser.parse_args()
server = ThreadingHTTPServer(('127.0.0.1', 8765), Handler)
thread = threading.Thread(target=server.serve_forever, daemon=True)
t0=time.perf_counter(); thread.start()
while True:
    try:
        import urllib.request
        urllib.request.urlopen('http://127.0.0.1:8765/health', timeout=1).read()
        break
    except Exception:
        time.sleep(.01)
startup=(time.perf_counter()-t0)*1000
print(f'Bare-metal/local process startup to first response: {startup:.2f} ms')
print(f'ApacheBench: ab -n {args.requests} -c {args.concurrency} http://127.0.0.1:8765/')
try:
    result=subprocess.run(['ab','-n',str(args.requests),'-c',str(args.concurrency),'-q','http://127.0.0.1:8765/'],
                          capture_output=True,text=True,timeout=120)
    print(result.stdout)
    if result.stderr: print(result.stderr)
finally:
    server.shutdown()
