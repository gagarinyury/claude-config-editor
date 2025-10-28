#!/usr/bin/env python3
"""
Claude Config Editor - Web-based editor for .claude.json configuration
"""

import http.server
import socketserver
import json
import os
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import sys

CLAUDE_CONFIG_PATH = Path.home() / '.claude.json'
PORT = 8765

class ClaudeConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/':
            self.send_html()
        elif parsed_path.path == '/api/config':
            self.send_config()
        elif parsed_path.path == '/api/project':
            self.send_project_history()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/save':
            self.save_config()
        else:
            self.send_response(404)
            self.end_headers()

    def send_project_history(self):
        """Export single project history as JSON"""
        try:
            query = parse_qs(urlparse(self.path).query)
            project_path = query.get('path', [''])[0]

            with open(CLAUDE_CONFIG_PATH, 'r', encoding='utf-8') as f:
                config = json.load(f)

            if project_path in config.get('projects', {}):
                project_data = config['projects'][project_path]

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Content-Disposition', f'attachment; filename="project-history.json"')
                self.end_headers()
                self.wfile.write(json.dumps(project_data, indent=2, ensure_ascii=False).encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {'error': str(e)}
            self.wfile.write(json.dumps(error).encode('utf-8'))

    def send_html(self):
        html_path = Path(__file__).parent / 'index.html'
        if html_path.exists():
            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
        else:
            # Fallback inline HTML
            html = self.get_inline_html()

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def get_inline_html(self):
        # Inline HTML as fallback
        return "<!DOCTYPE html><html><body><h1>Error: index.html not found</h1></body></html>"

    def send_config(self):
        try:
            with open(CLAUDE_CONFIG_PATH, 'r', encoding='utf-8') as f:
                config = json.load(f)

            response = {
                'path': str(CLAUDE_CONFIG_PATH),
                'config': config
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {'error': str(e)}
            self.wfile.write(json.dumps(error).encode('utf-8'))

    def save_config(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            new_config = json.loads(body.decode('utf-8'))

            # Create backup
            backup_path = CLAUDE_CONFIG_PATH.with_suffix('.json.backup')
            if CLAUDE_CONFIG_PATH.exists():
                import shutil
                shutil.copy2(CLAUDE_CONFIG_PATH, backup_path)

            # Save
            with open(CLAUDE_CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(new_config, f, indent=2, ensure_ascii=False)

            response = {'success': True, 'backup': str(backup_path)}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {'success': False, 'error': str(e)}
            self.wfile.write(json.dumps(error).encode('utf-8'))

    def log_message(self, format, *args):
        # Suppress default logging
        pass

def main():
    if not CLAUDE_CONFIG_PATH.exists():
        print(f"❌ Config file not found: {CLAUDE_CONFIG_PATH}")
        print(f"   Please ensure Claude Code is installed and has been run at least once.")
        sys.exit(1)

    print("🚀 Claude Config Editor")
    print(f"📁 Config: {CLAUDE_CONFIG_PATH}")
    print(f"🌐 Server: http://localhost:{PORT}")
    print(f"\n✨ Open your browser and navigate to the URL above")
    print(f"   Press Ctrl+C to stop\n")

    try:
        with socketserver.TCPServer(("", PORT), ClaudeConfigHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"\n❌ Port {PORT} is already in use.")
            print(f"   Try closing any existing instances or use a different port.")
            sys.exit(1)
        else:
            raise

if __name__ == '__main__':
    main()
