from __future__ import annotations
import base64, json, os, secrets, socket, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

class DeviceHub:
    """Small authenticated LAN hub for JARVIS <-> Android devices."""
    def __init__(self, host='0.0.0.0', port=8765):
        self.host, self.port = host, port
        self.key = secrets.token_urlsafe(18)
        self.server = None
        self.thread = None
        self.events = []
        self.lock = threading.Lock()
        self.devices = {}
        self.camera_url = ''
        self.command_callback = None
        self.notification_callback = None

    def local_url(self):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.connect(('8.8.8.8',80)); ip=s.getsockname()[0]; s.close()
        except Exception: ip='127.0.0.1'
        return f'http://{ip}:{self.port}'

    def push(self, event):
        event=dict(event); event.setdefault('id',secrets.token_hex(6)); event.setdefault('ts',time.time())
        with self.lock: self.events.append(event); self.events=self.events[-100:]
        return event

    def pop_events(self, device_id, limit=20):
        with self.lock:
            out=[e for e in self.events if e.get('target') in (None, device_id)]
            self.events=[e for e in self.events if e not in out]
        return out[:limit]

    def start(self, command_callback=None, notification_callback=None):
        self.command_callback=command_callback
        self.notification_callback=notification_callback
        hub=self
        class H(BaseHTTPRequestHandler):
            def _json(self, code, data):
                raw=json.dumps(data).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw)
            def _auth(self): return self.headers.get('X-JARVIS-Key','') == hub.key
            def do_GET(self):
                path=urlparse(self.path).path
                if path in ('/','/index.html'):
                    page=hub._page(); raw=page.encode(); self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw); return
                if not self._auth(): self._json(401,{'error':'unauthorized'}); return
                if path=='/api/status':
                    with hub.lock: devices=dict(hub.devices)
                    self._json(200,{'ok':True,'devices':devices,'camera_url':hub.camera_url,'url':hub.local_url()}); return
                if path=='/api/events':
                    qs={k:v[0] for k,v in __import__('urllib.parse').parse_qs(urlparse(self.path).query).items()}
                    self._json(200,{'events':hub.pop_events(qs.get('device','unknown'))}); return
                if path=='/camera':
                    if not hub.camera_url: self._json(404,{'error':'no camera configured'}); return
                    self.send_response(302); self.send_header('Location',hub.camera_url); self.end_headers(); return
                self._json(404,{'error':'not found'})
            def do_POST(self):
                if not self._auth(): self._json(401,{'error':'unauthorized'}); return
                try: n=int(self.headers.get('Content-Length','0')); body=json.loads(self.rfile.read(n) or b'{}')
                except Exception: self._json(400,{'error':'invalid json'}); return
                path=urlparse(self.path).path
                if path=='/api/register':
                    did=str(body.get('device_id','android')); name=str(body.get('name',did))
                    with hub.lock: hub.devices[did]={'name':name,'last_seen':time.time(),'type':body.get('type','android')}
                    self._json(200,{'ok':True,'device_id':did}); return
                if path=='/api/notify':
                    ev={'type':'notification','source':body.get('source','phone'),'title':body.get('title',''),'text':body.get('text',''),'target':None}
                    hub.push(ev)
                    if hub.notification_callback:
                        try: hub.notification_callback(ev)
                        except Exception: pass
                    self._json(200,{'ok':True}); return
                if path=='/api/command':
                    cmd=body.get('command') or body
                    if hub.command_callback:
                        try: result=hub.command_callback(cmd)
                        except Exception as e: result={'ok':False,'error':str(e)}
                    else: result={'ok':False,'error':'no callback'}
                    self._json(200,result if isinstance(result,dict) else {'ok':True,'result':result}); return
                if path=='/api/event':
                    ev=dict(body); ev.setdefault('target',body.get('target')); hub.push(ev); self._json(200,{'ok':True}); return
                if path=='/api/camera':
                    hub.camera_url=str(body.get('url','')).strip(); self._json(200,{'ok':True,'camera_url':hub.camera_url}); return
                self._json(404,{'error':'not found'})
            def log_message(self,*a): pass
        self.server=ThreadingHTTPServer((self.host,self.port),H)
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True,name='jarvis-device-hub'); self.thread.start(); return self.local_url(), self.key

    def _page(self):
        return '''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>JARVIS Device Hub</title><style>body{background:#02080d;color:#8ffcff;font-family:monospace;margin:20px}button,input{background:#06131b;color:#8ffcff;border:1px solid #17607b;padding:12px;margin:4px;border-radius:4px}h1{letter-spacing:3px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}pre{white-space:pre-wrap}</style></head><body><h1>J.A.R.V.I.S DEVICE HUB</h1><p>Use the Android companion app with this hub URL and key.</p><div class="grid"><button onclick="cmd('media','play_pause')">PLAY / PAUSE</button><button onclick="cmd('media','next')">NEXT</button><button onclick="cmd('media','previous')">PREVIOUS</button><button onclick="cmd('volume','up')">VOL +</button><button onclick="cmd('volume','down')">VOL -</button><button onclick="cmd('volume','mute')">MUTE</button></div><input id="app" placeholder="Android app: youtube"><button onclick="launch()">LAUNCH</button><input id="cam" placeholder="IP camera MJPEG URL"><button onclick="camera()">SET CAMERA</button><pre id="log"></pre><script>const key=new URLSearchParams(location.search).get('key')||prompt('JARVIS key');async function post(p,b){let r=await fetch(p,{method:'POST',headers:{'Content-Type':'application/json','X-JARVIS-Key':key},body:JSON.stringify(b)});return r.json()}function cmd(type,action){post('/api/command',{command:{type,action}}).then(x=>log(x))}function launch(){post('/api/event',{type:'launch_app',app:document.getElementById('app').value,target:'android'}).then(log)}function camera(){post('/api/camera',{url:document.getElementById('cam').value}).then(log)}function log(x){document.getElementById('log').textContent=JSON.stringify(x,null,2)}</script></body></html>'''
