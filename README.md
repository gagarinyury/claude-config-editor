# 🚀 Claude Config Editor

**The missing GUI for Claude configurations**

A beautiful, fast, and powerful web-based editor for both **Claude Code** and **Claude Desktop** configuration files. Clean up bloated configs, manage MCP servers, and export project histories—all from your browser.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)

---

## ✨ Why You Need This

Your Claude config is **probably bloated**. Mine was **17 MB** before I built this tool—now it's **732 KB**.

Claude stores your entire conversation history for every project. Over time, this adds up:
- 📁 **87 projects** with full chat histories
- 💾 **17 MB** of JSON
- 🐌 Slower startup times
- 🔍 Hard to find what's taking space

**This tool fixes that.**

---

## 🎯 Features

### 📊 Smart Analytics
- Instant config health check
- Size breakdown by project
- Quick recommendations

### 📁 Project History Manager
- See which projects are eating your disk space
- Export individual project histories before deletion
- Bulk delete old/unused projects
- Sort by size, name, or message count
- Search and filter projects

### 🔌 MCP Server Management
- Visual list of all MCP servers
- Add/remove servers with one click
- See command, args, env, and working directory
- No more manual JSON editing

### 🎨 Beautiful Interface
- Dark theme (easy on the eyes)
- Real-time updates
- Responsive design
- No installation required

### 🔒 Safety First
- Automatic backups before every save
- Preview changes before applying
- Non-destructive operations
- Works on a local copy

---

## 🚄 Quick Start

**One command. No dependencies. No BS.**

```bash
# Clone and run
git clone https://github.com/yourusername/claude-config-editor.git
cd claude-config-editor
python3 server.py

# That's it. Opens at http://localhost:8765
```

### Auto-Detection
The tool automatically detects:
- ✅ Claude Code config (`~/.claude.json`)
- ✅ Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`)

If both exist, you'll be prompted to choose which one to edit.

---

## 💡 Common Use Cases

### "My Claude Code startup is slow"
→ Your config is probably huge. Use this tool to delete old project histories.

### "I want to backup my MCP servers"
→ Go to "MCP Servers" tab, see all your servers, then click "Backup" to download.

### "I want to export my conversation with Claude from project X"
→ Go to "Project History", find your project, click "💾 Export". Done.

### "I don't know which MCP servers I have installed"
→ Open the tool, go to "MCP Servers" tab. See them all at a glance.

---

## 📖 How to Use

### 1️⃣ Clean Up Project History

Your `.claude.json` stores **every conversation** from **every project**. This is the #1 reason for bloat.

**Steps:**
1. Open the tool
2. Go to **"Project History"** tab
3. Click **"Top 10 Largest"** (selects biggest projects)
4. Review selected projects
5. Click **"Delete Selected"**
6. Click **"💾 Save Changes"**

**Result:** Reduce your config from 17 MB → 732 KB (like I did)

**Safety:** Each project has an **"💾 Export"** button to save history before deletion.

---

### 2️⃣ Manage MCP Servers

**View all MCP servers:**
```
🔌 code-index
   Command: uv
   Args: ["run", "code-index-mcp"]
   CWD: /Users/you/code/code-index-mcp

🔌 playwright
   Command: npx
   Args: ["@playwright/mcp@latest"]
```

**Add a server:**
1. Click **"+ Add Server"**
2. Enter name & command
3. Save

**Remove a server:**
1. Find the server card
2. Click **"Delete"**
3. Save

---

### 3️⃣ Export Project History

Want to keep a conversation history before deleting?

1. Go to **"Project History"**
2. Find your project
3. Click **"💾 Export"** (downloads JSON file)
4. Now safe to delete

---

## 🛡️ Safety

- ✅ **Auto-backup** before every save
- ✅ **Non-destructive** - only modifies what you tell it to
- ✅ **Local-only** - no data leaves your machine
- ✅ **Read-only mode** - browse without risk

**Backup location:** `.claude.backup.json` (created automatically)

---

## 🔧 Technical Details

### Supported Configs

| Config | Path | Supported |
|--------|------|-----------|
| Claude Code (macOS/Linux) | `~/.claude.json` | ✅ |
| Claude Code (Windows) | `%USERPROFILE%\.claude.json` | ✅ |
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` | ✅ |
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` | ✅ |
| Claude Desktop (Linux) | `~/.config/Claude/claude_desktop_config.json` | ✅ |

### Requirements
- **Python 3.7+** (uses only stdlib - no pip install needed)
- **Claude Code** or **Claude Desktop** installed

### How It Works
1. Starts local HTTP server (port 8765)
2. Loads config via REST API
3. Provides web UI for editing
4. Saves changes back to config file
5. Creates automatic backup

---

## 🎓 FAQ

**Q: Will this break my Claude setup?**
A: No. The tool only modifies what you explicitly tell it to. Plus, automatic backups are created.

**Q: Do I need to restart Claude after making changes?**
A: Yes. Changes take effect after restarting Claude Code/Desktop.

**Q: Is my data sent anywhere?**
A: Nope. Everything runs locally on `localhost:8765`. Zero network requests.

**Q: What if I delete the wrong project?**
A: Use the **"💾 Export"** button first to save a copy. Or restore from `.claude.backup.json`.

**Q: Can I use this on Windows?**
A: Yes! Works on macOS, Linux, and Windows.

**Q: Does this work with Claude Desktop?**
A: Yes! It supports both Claude Code (`.claude.json`) and Claude Desktop (`claude_desktop_config.json`).

---

## 🤝 Contributing

Found a bug? Have an idea? PRs welcome!

```bash
# Fork the repo, then:
git clone https://github.com/yourusername/claude-config-editor.git
cd claude-config-editor
# Make your changes
git commit -am "Add awesome feature"
git push origin main
# Open a PR
```

---

## 📜 License

MIT License - do whatever you want with this.

---

## 🙏 Acknowledgments

Built with frustration after my `.claude.json` hit 17 MB and I couldn't figure out why Claude Code was slow.

Turned out it was **87 projects** worth of conversation history. This tool fixed it in 30 seconds.

**If this saved you time, star the repo! ⭐**

---

## 🐛 Known Issues

None yet. Open an issue if you find one.

---

## 🗺️ Roadmap

- [ ] Search/filter in Raw JSON view
- [ ] Edit MCP server parameters inline
- [ ] Import project history from JSON
- [ ] Config diff viewer
- [ ] Automatic cleanup suggestions

---

## 💬 Support

- 🐛 **Bug reports:** [Open an issue](https://github.com/yourusername/claude-config-editor/issues)
- 💡 **Feature requests:** [Open an issue](https://github.com/yourusername/claude-config-editor/issues)
- 📧 **Questions:** [Discussions](https://github.com/yourusername/claude-config-editor/discussions)

---

<p align="center">
Made with ❤️ and Claude Code
</p>

<p align="center">
If this tool helped you, consider <a href="https://github.com/yourusername/claude-config-editor">starring the repo</a>!
</p>
