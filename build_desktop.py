#!/usr/bin/env python3
"""
Build script for creating standalone desktop executables.
Supports: macOS, Linux, Windows

Usage:
    python build_desktop.py
"""

import sys
import platform
import subprocess
import shutil
from pathlib import Path

def check_requirements():
    """Check if build requirements are installed."""
    missing = []

    try:
        import PyInstaller
    except ImportError:
        missing.append('pyinstaller')

    try:
        import webview
    except ImportError:
        missing.append('pywebview')

    if missing:
        print(f"❌ Missing requirements: {', '.join(missing)}")
        print("\nInstall with:")
        print("  pip install -r requirements-build.txt\n")
        return False

    return True

def clean_build():
    """Clean previous build artifacts."""
    dirs = ['build', 'dist', '__pycache__']
    for d in dirs:
        if Path(d).exists():
            print(f"🧹 Cleaning {d}/")
            shutil.rmtree(d)

    # Remove spec files
    for spec in Path('.').glob('*.spec'):
        print(f"🧹 Removing {spec}")
        spec.unlink()

def build():
    """Build executable for current platform."""
    if not check_requirements():
        sys.exit(1)

    system = platform.system()

    print("🔨 Building Claude Config Editor Desktop...")
    print(f"   Platform: {system}\n")

    # Clean previous builds
    clean_build()

    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--name=ClaudeConfigEditor',
        '--onefile',                    # Single executable
        '--windowed',                   # No console window (GUI app)
        '--add-data=index.html:.',     # Bundle HTML file
        '--hidden-import=webview',
        '--hidden-import=webview.platforms.gtk',      # Linux
        '--hidden-import=webview.platforms.qt',       # Linux fallback
        '--hidden-import=webview.platforms.cocoa',    # macOS
        '--hidden-import=webview.platforms.winforms', # Windows
        'server.py'
    ]

    # Platform-specific adjustments
    if system == 'Darwin':
        print("📦 Building for macOS...")
        cmd.extend([
            '--osx-bundle-identifier=com.claude.configeditor',
        ])
    elif system == 'Windows':
        print("📦 Building for Windows...")
    elif system == 'Linux':
        print("📦 Building for Linux...")
    else:
        print(f"⚠️  Untested platform: {system}")

    # Run PyInstaller
    print("⏳ Building... (this may take a few minutes)\n")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        exe_name = 'ClaudeConfigEditor.exe' if system == 'Windows' else 'ClaudeConfigEditor'
        exe_path = Path('dist') / exe_name

        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print("\n✅ Build successful!")
            print(f"📂 Output: {exe_path}")
            print(f"📊 Size: {size_mb:.1f} MB\n")

            print("🧪 Test the executable:")
            if system == 'Windows':
                print(f"   .\\dist\\{exe_name} --help\n")
            else:
                print(f"   ./dist/{exe_name} --help\n")
        else:
            print("\n❌ Build completed but executable not found!")
            sys.exit(1)
    else:
        print("\n❌ Build failed!")
        print("   Check errors above for details.")
        sys.exit(1)

if __name__ == '__main__':
    build()
