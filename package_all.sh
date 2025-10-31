#!/bin/bash
# Automated packaging script for Claude Config Editor
# Detects platform and creates appropriate package

set -e

echo "📦 Claude Config Editor - Packaging Script"
echo ""

# Detect platform
PLATFORM=$(uname -s)
PACKAGES_DIR="packages"

# Clean and create packages directory
rm -rf "$PACKAGES_DIR"
mkdir -p "$PACKAGES_DIR"

# Check if build_desktop.py exists
if [ ! -f "build_desktop.py" ]; then
    echo "❌ Error: build_desktop.py not found"
    echo "   Make sure you're in the project root directory"
    exit 1
fi

# Check if requirements-build.txt exists
if [ ! -f "requirements-build.txt" ]; then
    echo "❌ Error: requirements-build.txt not found"
    exit 1
fi

# Check if dependencies are installed
echo "🔍 Checking dependencies..."
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "📥 Installing build dependencies..."
    pip install -r requirements-build.txt
fi

# Build executable
echo ""
echo "🔨 Building executable for $PLATFORM..."
echo ""
python3 build_desktop.py

if [ ! -d "dist" ]; then
    echo "❌ Error: dist/ directory not found after build"
    exit 1
fi

# Platform-specific packaging
case "$PLATFORM" in
    Darwin)
        echo ""
        echo "📦 Creating macOS package..."
        cd dist
        if [ ! -d "ClaudeConfigEditor.app" ]; then
            echo "❌ Error: ClaudeConfigEditor.app bundle not found in dist/"
            exit 1
        fi
        zip -r "../$PACKAGES_DIR/ClaudeConfigEditor-macOS.zip" "ClaudeConfigEditor.app"
        cd ..

        SIZE=$(du -h "$PACKAGES_DIR/ClaudeConfigEditor-macOS.zip" | cut -f1)
        echo "✅ macOS package created: ClaudeConfigEditor-macOS.zip ($SIZE)"
        ;;

    Linux)
        echo ""
        echo "📦 Creating Linux package..."

        # Check if AppImage tool is available
        if ! command -v appimagetool &> /dev/null; then
            echo "⚠️  Warning: appimagetool not found"
            echo "   Creating simple ZIP package instead"
            echo "   For AppImage: see docs/QUICK_BUILD_AND_PACKAGE.md"

            cd dist
            zip -r "../$PACKAGES_DIR/ClaudeConfigEditor-Linux.zip" ClaudeConfigEditor
            cd ..

            SIZE=$(du -h "$PACKAGES_DIR/ClaudeConfigEditor-Linux.zip" | cut -f1)
            echo "✅ Linux package created: ClaudeConfigEditor-Linux.zip ($SIZE)"
        else
            # Create AppDir structure
            rm -rf ClaudeConfigEditor.AppDir
            mkdir -p ClaudeConfigEditor.AppDir/usr/bin
            mkdir -p ClaudeConfigEditor.AppDir/usr/share/applications

            # Copy executable
            cp dist/ClaudeConfigEditor ClaudeConfigEditor.AppDir/usr/bin/

            # Create desktop entry
            cat > ClaudeConfigEditor.AppDir/claude-config-editor.desktop <<'EOF'
[Desktop Entry]
Name=Claude Config Editor
Exec=ClaudeConfigEditor
Type=Application
Categories=Utility;Settings;
Comment=Edit Claude Code and Desktop configurations
Terminal=false
EOF

            # Copy to root
            cp ClaudeConfigEditor.AppDir/claude-config-editor.desktop ClaudeConfigEditor.AppDir/

            # Create AppRun
            cat > ClaudeConfigEditor.AppDir/AppRun <<'EOF'
#!/bin/bash
SELF=$(readlink -f "$0")
HERE=${SELF%/*}
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"
exec "${HERE}/usr/bin/ClaudeConfigEditor" "$@"
EOF

            chmod +x ClaudeConfigEditor.AppDir/AppRun

            # Build AppImage
            appimagetool ClaudeConfigEditor.AppDir "$PACKAGES_DIR/ClaudeConfigEditor-x86_64.AppImage"

            SIZE=$(du -h "$PACKAGES_DIR/ClaudeConfigEditor-x86_64.AppImage" | cut -f1)
            echo "✅ Linux AppImage created: ClaudeConfigEditor-x86_64.AppImage ($SIZE)"
        fi
        ;;

    *)
        echo "❌ Unsupported platform: $PLATFORM"
        echo "   This script supports macOS (Darwin) and Linux"
        echo "   For Windows, run manually:"
        echo "     python build_desktop.py"
        echo "     powershell Compress-Archive dist\\ClaudeConfigEditor.exe packages\\ClaudeConfigEditor-Windows.zip"
        exit 1
        ;;
esac

# List created packages
echo ""
echo "📂 Packages created in: $PACKAGES_DIR/"
ls -lh "$PACKAGES_DIR/"

# Next steps
echo ""
echo "✨ Next steps:"
echo "   1. Test the package:"
case "$PLATFORM" in
    Darwin)
        echo "      cd /tmp && unzip $(pwd)/$PACKAGES_DIR/ClaudeConfigEditor-macOS.zip"
        echo "      ./ClaudeConfigEditor --desktop"
        ;;
    Linux)
        if command -v appimagetool &> /dev/null; then
            echo "      chmod +x $PACKAGES_DIR/ClaudeConfigEditor-x86_64.AppImage"
            echo "      ./$PACKAGES_DIR/ClaudeConfigEditor-x86_64.AppImage --desktop"
        else
            echo "      cd /tmp && unzip $(pwd)/$PACKAGES_DIR/ClaudeConfigEditor-Linux.zip"
            echo "      ./ClaudeConfigEditor --desktop"
        fi
        ;;
esac
echo ""
echo "   2. Create GitHub release:"
echo "      gh release create v2.1.0 $PACKAGES_DIR/*"
echo ""
echo "   See docs/GITHUB_RELEASE_WORKFLOW.md for details"
echo ""
