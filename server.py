#!/usr/bin/env python3
"""
Claude Config Editor - Universal web-based editor for Claude configurations
Supports both Claude Code (.claude.json) and Claude Desktop (claude_desktop_config.json)
"""

import http.server
import socketserver
import json
import os
import sys
import platform
import argparse
import threading
import time
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Conditional import for PyWebView
try:
    import webview
    WEBVIEW_AVAILABLE = True
except ImportError:
    WEBVIEW_AVAILABLE = False

PORT = 8765

# Detect config files
def detect_configs():
    """Detect available Claude configuration files"""
    configs = {}

    # Claude Code config
    claude_code_path = Path.home() / '.claude.json'
    if claude_code_path.exists():
        configs['code'] = {
            'path': claude_code_path,
            'name': 'Claude Code (CLI)',
            'type': 'code'
        }

    # Claude Desktop config
    if platform.system() == 'Darwin':  # macOS
        claude_desktop_path = Path.home() / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json'
    elif platform.system() == 'Windows':
        claude_desktop_path = Path(os.environ['APPDATA']) / 'Claude' / 'claude_desktop_config.json'
    else:  # Linux
        claude_desktop_path = Path.home() / '.config' / 'Claude' / 'claude_desktop_config.json'

    if claude_desktop_path.exists():
        configs['desktop'] = {
            'path': claude_desktop_path,
            'name': 'Claude Desktop',
            'type': 'desktop'
        }

    return configs

# Global config path (set on startup)
ACTIVE_CONFIG = None

class ClaudeConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/':
            self.send_html()
        elif parsed_path.path == '/api/config':
            self.send_config()
        elif parsed_path.path == '/api/project':
            self.send_project_history()
        elif parsed_path.path == '/api/configs':
            self.send_available_configs()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/save':
            self.save_config()
        elif self.path == '/api/switch':
            self.switch_config()
        else:
            self.send_response(404)
            self.end_headers()

    def send_available_configs(self):
        """Send list of available configs"""
        configs = detect_configs()
        config_list = [
            {
                'id': key,
                'name': val['name'],
                'path': str(val['path']),
                'type': val['type'],
                'active': ACTIVE_CONFIG['path'] == val['path']
            }
            for key, val in configs.items()
        ]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(config_list).encode('utf-8'))

    def switch_config(self):
        """Switch active config"""
        global ACTIVE_CONFIG

        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            config_id = data.get('config_id')

            configs = detect_configs()
            if config_id in configs:
                ACTIVE_CONFIG = configs[config_id]

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'success': True, 'config': str(ACTIVE_CONFIG['path'])}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                raise ValueError('Invalid config ID')
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {'success': False, 'error': str(e)}
            self.wfile.write(json.dumps(error).encode('utf-8'))

    def send_project_history(self):
        """Export single project history as JSON"""
        try:
            query = parse_qs(urlparse(self.path).query)
            project_path = query.get('path', [''])[0]

            with open(ACTIVE_CONFIG['path'], 'r', encoding='utf-8') as f:
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
            html = "<!DOCTYPE html><html><body><h1>Error: index.html not found</h1></body></html>"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def send_config(self):
        try:
            with open(ACTIVE_CONFIG['path'], 'r', encoding='utf-8') as f:
                config = json.load(f)

            response = {
                'path': str(ACTIVE_CONFIG['path']),
                'name': ACTIVE_CONFIG['name'],
                'type': ACTIVE_CONFIG['type'],
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
            backup_path = ACTIVE_CONFIG['path'].parent / f"{ACTIVE_CONFIG['path'].stem}.backup{ACTIVE_CONFIG['path'].suffix}"
            if ACTIVE_CONFIG['path'].exists():
                import shutil
                shutil.copy2(ACTIVE_CONFIG['path'], backup_path)

            # Save
            with open(ACTIVE_CONFIG['path'], 'w', encoding='utf-8') as f:
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
        pass

def select_config():
    """Interactive config selection"""
    configs = detect_configs()

    if not configs:
        print("❌ No Claude configuration files found!")
        print("\nPlease ensure Claude Code or Claude Desktop is installed and configured.")
        sys.exit(1)

    if len(configs) == 1:
        # Only one config found, use it
        config_id = list(configs.keys())[0]
        return configs[config_id]

    # Multiple configs found, let user choose
    print("\n🔍 Found multiple Claude configurations:\n")
    for i, (key, val) in enumerate(configs.items(), 1):
        size = val['path'].stat().st_size if val['path'].exists() else 0
        size_mb = size / (1024 * 1024)
        print(f"  {i}. {val['name']}")
        print(f"     Path: {val['path']}")
        print(f"     Size: {size_mb:.2f} MB\n")

    while True:
        try:
            choice = input(f"Select config (1-{len(configs)}) or press Enter for default [1]: ").strip()
            if not choice:
                choice = '1'
            choice_num = int(choice)
            if 1 <= choice_num <= len(configs):
                config_id = list(configs.keys())[choice_num - 1]
                return configs[config_id]
            else:
                print(f"Please enter a number between 1 and {len(configs)}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Cancelled")
            sys.exit(0)

def start_server_thread(port=0):
    """
    Start HTTP server in background thread and return the actual port used.

    Args:
        port: Port to use (0 = random available port)

    Returns:
        int: The actual port the server is listening on
    """
    class ServerThread(threading.Thread):
        def __init__(self, port):
            super().__init__(daemon=True)
            self.port = port
            self.httpd = None
            self.ready = threading.Event()

        def run(self):
            with socketserver.TCPServer(("127.0.0.1", self.port), ClaudeConfigHandler) as httpd:
                self.httpd = httpd
                # If port was 0, get the actual assigned port
                if self.port == 0:
                    self.port = httpd.server_address[1]
                self.ready.set()  # Signal that server is ready
                httpd.serve_forever()

    thread = ServerThread(port)
    thread.start()
    thread.ready.wait()  # Wait for server to be ready

    return thread.port

def run_desktop_mode():
    """Run application in desktop window mode using PyWebView."""
    global ACTIVE_CONFIG

    # Check if PyWebView is available
    if not WEBVIEW_AVAILABLE:
        print("❌ PyWebView not installed!")
        print("\n   Desktop mode requires PyWebView.")
        print("   Install with: pip install pywebview\n")
        print("   Or use browser mode: python3 server.py")
        sys.exit(1)

    print("🚀 Claude Config Editor (Desktop Mode)")
    print("   Universal editor for Claude Code & Claude Desktop\n")

    # Select config (interactive or from ACTIVE_CONFIG if already set)
    if ACTIVE_CONFIG is None:
        ACTIVE_CONFIG = select_config()

    print(f"\n✅ Active config: {ACTIVE_CONFIG['name']}")
    print(f"📁 Path: {ACTIVE_CONFIG['path']}")

    size = ACTIVE_CONFIG['path'].stat().st_size
    size_mb = size / (1024 * 1024)
    print(f"📊 Size: {size_mb:.2f} MB")
    print(f"\n🪟 Opening desktop window...\n")

    # Start server on random port (avoids conflicts)
    port = start_server_thread(port=0)

    # Create desktop window
    webview.create_window(
        title='Claude Config Editor',
        url=f'http://127.0.0.1:{port}',
        width=1400,
        height=900,
        resizable=True,
        min_size=(1000, 700),
        background_color='#1e1e1e'
    )

    # Start PyWebView event loop (blocks until window closes)
    webview.start(debug=False)

    print("\n👋 Window closed. Goodbye!")

def main():
    global ACTIVE_CONFIG

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Claude Config Editor - Edit Claude Code & Desktop configurations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 server.py                    # Browser mode (interactive)
  python3 server.py code               # Browser mode (Claude Code config)
  python3 server.py desktop            # Browser mode (Claude Desktop config)
  python3 server.py --desktop          # Desktop window mode (interactive)
  python3 server.py --desktop code     # Desktop window mode (Claude Code config)
        """
    )

    parser.add_argument(
        '--desktop',
        action='store_true',
        help='Run in desktop window mode (requires pywebview)'
    )

    parser.add_argument(
        'config_type',
        nargs='?',
        choices=['code', 'desktop'],
        help='Config type to edit (code or desktop)'
    )

    args = parser.parse_args()

    # Pre-select config if specified via argument
    if args.config_type:
        configs = detect_configs()
        if args.config_type in configs:
            ACTIVE_CONFIG = configs[args.config_type]
        else:
            print(f"❌ Config type '{args.config_type}' not found.")
            print(f"   Available: {', '.join(configs.keys())}")
            sys.exit(1)

    # Route to appropriate mode
    if args.desktop:
        run_desktop_mode()
        return

    # Browser mode (original behavior)
    print("🚀 Claude Config Editor")
    print("   Universal editor for Claude Code & Claude Desktop\n")

    # Interactive config selection if not already set
    if ACTIVE_CONFIG is None:
        ACTIVE_CONFIG = select_config()

    print(f"\n✅ Active config: {ACTIVE_CONFIG['name']}")
    print(f"📁 Path: {ACTIVE_CONFIG['path']}")

    size = ACTIVE_CONFIG['path'].stat().st_size
    size_mb = size / (1024 * 1024)
    print(f"📊 Size: {size_mb:.2f} MB")

    print(f"\n🌐 Server: http://localhost:{PORT}")
    print(f"\n✨ Open your browser and navigate to the URL above")
    print(f"   Press Ctrl+C to stop\n")

    try:
        with socketserver.TCPServer(("", PORT), ClaudeConfigHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Port in use (macOS/Linux)
            print(f"\n❌ Port {PORT} is already in use.")
            print(f"   Try:")
            print(f"   1. Close any existing instances")
            print(f"   2. Use desktop mode: python3 server.py --desktop")
            sys.exit(1)
        else:
            raise

if __name__ == '__main__':
    main()
