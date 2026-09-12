#!/usr/bin/env python3
import http.server, mimetypes, os, sys

mimetypes.add_type("model/gltf+json", ".gltf")
mimetypes.add_type("model/gltf-binary", ".glb")
mimetypes.add_type("application/octet-stream", ".bin")

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

with http.server.HTTPServer(("", PORT), CORSHandler) as server:
    print(f"Serving {os.getcwd()} on http://localhost:{PORT}")
    server.serve_forever()
