# 🚀 Claude Config Editor

<p align="center">
  <img src="https://img.shields.io/badge/Your%20.claude.json%20is-BLOATED-red?style=for-the-badge" alt="Bloated">
  <img src="https://img.shields.io/badge/This%20fixes%20it-IN%2030%20SECONDS-green?style=for-the-badge" alt="Fixed">
</p>

<h3 align="center">⚡ The missing GUI for Claude configurations ⚡</h3>

<p align="center">
  <strong>Your Claude config is probably 10+ MB.</strong><br>
  <strong>Mine was 17 MB.</strong> Now it's <strong>732 KB</strong>.<br>
  <strong>This tool did it in 30 seconds.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/dependencies-ZERO-brightgreen.svg" alt="Zero Dependencies">
</p>

---

## 🔥 The Problem

**Claude Code stores EVERY conversation from EVERY project** in a single JSON file.

After a few weeks of use:
- 📁 87 projects with full chat histories
- 💾 **17 MB** of JSON (yes, really)
- 🐌 **Slow startup times** (Claude has to parse that mess)
- 🤷 **No easy way to clean it up** (manual JSON editing? no thanks)

**Sound familiar?**

## ✅ The Solution

A beautiful web interface to:
- 🔍 **See what's eating your disk** (sorted by size)
- 🗑️ **Delete old projects in bulk** (top 10 biggest = 90% of bloat)
- 💾 **Export before deleting** (keep important conversations)
- 🔌 **Manage MCP servers** (no more JSON editing)
- 🛡️ **Auto-backup everything** (undo button for real life)

**Works with both Claude Code AND Claude Desktop.**

---

## 🎯 Why People Star This Repo

> "My .claude.json was 23 MB. Deleted 50 old projects. Now it's 1.8 MB. Claude Code starts instantly now." - *Actual result*

> "Finally! I can see my MCP servers without opening VSCode." - *Reddit user*

> "I didn't even know this was a problem until I ran this tool." - *HN comment*

**Translation:** This tool solves a problem you didn't know you had, in 30 seconds, with zero risk.

---

## 🚄 Quick Start

**Three commands. Zero dependencies. Zero configuration.**

```bash
git clone https://github.com/gagarinyury/claude-config-editor.git
cd claude-config-editor
python3 server.py
```

**That's it.** Opens at `http://localhost:8765`.

### What Happens Next

1. **Tool auto-detects** your configs (Claude Code + Claude Desktop)
2. **You select** which one to edit
3. **30 seconds later** your config is clean and fast

---

## ✨ Features That Make You Go "Finally!"

### 📊 Smart Analytics
See **exactly** what's taking up space:
- Config size (before/after)
- Projects ranked by size (biggest first)
- Instant health check ("Your config is bloated AF")

### 📁 Project History Manager
The killer feature:
- **Export individual project histories** before deletion (download as JSON)
- **Bulk delete old projects** (select top 10 = 90% space saved)
- **Search & filter** (find that old client project from 6 months ago)
- **Sort by size/name/messages** (find the bloat faster)

### 🔌 MCP Server Management
Because editing JSON manually is for masochists:
- **Visual list** of all MCP servers
- **See command, args, env, working directory** at a glance
- **Add/remove servers** with one click
- **No more typos** in JSON (you know what I'm talking about)

### 🎨 Beautiful Interface
- Dark theme (because your eyes matter)
- Real-time updates (see changes as you make them)
- Responsive (works on your tiny laptop screen)
- **No installation required** (Python stdlib only)

### 🔒 Safety First
- **Auto-backup before every save** (undo button for real life)
- **Non-destructive** (only changes what you tell it to)
- **Local-only** (zero network requests, zero data collection)
- **Preview before save** (see what you're about to do)

---

## 💡 Real-World Use Cases

### "My Claude Code is slow"
→ Your config is probably huge. Click "Top 10 Largest", delete, save. Done in 30 seconds.

### "I want to backup my conversations"
→ Go to Project History, click "💾 Export" on any project. Downloads JSON. Keep forever.

### "I don't know which MCP servers I have"
→ Go to MCP Servers tab. See everything. No more `cat ~/.claude.json | grep mcpServers`.

### "I messed up my config"
→ Restore from `.claude.backup.json` (created automatically before every save).

### "I want to share my setup"
→ Export your config, share the JSON. Or just share this tool.

---

## 📖 How It Works (30 Second Tutorial)

### Clean Up Project History

```
1. Open tool → Go to "Project History"
2. Click "Top 10 Largest" (selects 90% of bloat)
3. Review → Click "Delete Selected"
4. Click "💾 Save Changes"
```

**Result:** 17 MB → 732 KB (actual result from my config)

### Export Before Delete

```
1. Find project in list
2. Click "💾 Export" (downloads JSON)
3. Now safe to delete (you have a backup)
```

### Manage MCP Servers

```
View:   See all servers, their commands, args, env
Add:    Click "+ Add Server" → Enter name & command → Save
Remove: Find server card → Click "Delete" → Save
```

---

## 🛡️ Safety & Trust

- ✅ **Auto-backup** before every save (`.claude.backup.json`)
- ✅ **Open source** (read the code, it's 300 lines)
- ✅ **No analytics** (zero tracking, zero telemetry)
- ✅ **Local-only** (runs on `localhost:8765`, no internet required)
- ✅ **Non-destructive** (only modifies what you explicitly delete)

**Worst case:** Restore from `.claude.backup.json`. **Best case:** Your Claude is fast again.

---

## 🔧 Technical Details

### Supported Configs

| Config | Path | Auto-Detect |
|--------|------|-------------|
| Claude Code (macOS/Linux) | `~/.claude.json` | ✅ |
| Claude Code (Windows) | `%USERPROFILE%\.claude.json` | ✅ |
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` | ✅ |
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` | ✅ |
| Claude Desktop (Linux) | `~/.config/Claude/claude_desktop_config.json` | ✅ |

### Requirements
- **Python 3.7+** (no pip install, no virtualenv, just works)
- **Claude Code** or **Claude Desktop** (obviously)

### How It Actually Works
1. Starts HTTP server on port 8765
2. Loads config via REST API (`/api/config`)
3. Web UI makes changes in memory
4. Click "Save" → writes to disk (with backup)
5. Restart Claude → changes take effect

**Source:** 300 lines of Python + 700 lines of HTML/CSS/JS. No frameworks. No build step. Just works.

---

## 🎓 FAQ (Questions You're About to Ask)

**Q: Will this break my Claude setup?**
A: No. Automatic backups + only changes what you delete. Worst case: restore from `.claude.backup.json`.

**Q: Why is my config so big?**
A: Claude stores EVERY message from EVERY project. 100 projects × 50 messages × 1 KB = 5 MB. Add paste content and it balloons to 10-20 MB.

**Q: What happens to my conversations?**
A: Project history = conversation history. Deleting a project = deleting its chat history. **Use "💾 Export" first if you want to keep it.**

**Q: Is my data sent anywhere?**
A: Nope. Runs on `localhost:8765`. Zero network requests. Check the code if you don't believe me.

**Q: Can I undo a delete?**
A: Before save? Yes (just refresh). After save? Restore from `.claude.backup.json` (created automatically).

**Q: Why not just edit the JSON manually?**
A: You could. Or you could use this and finish in 30 seconds instead of 30 minutes of JSON hell.

**Q: Does this work with Claude Desktop?**
A: Yes! Auto-detects both Claude Code (`.claude.json`) and Claude Desktop (`claude_desktop_config.json`).

**Q: Can I run this on Windows?**
A: Yes! Python is cross-platform. Works on macOS, Linux, Windows.

---

## 🤝 Contributing

**Found a bug?** Open an issue.
**Have an idea?** Open an issue.
**Want to add a feature?** Fork + PR.

```bash
git clone https://github.com/gagarinyury/claude-config-editor.git
cd claude-config-editor
# Make your changes
git commit -am "Add awesome feature"
git push origin main
# Open PR
```

**Code style:** Keep it simple. This is a tool, not a framework.

---

## 📜 License

MIT License - do whatever you want with this code.

---

## 🙏 Origin Story

I built this because:

1. My Claude Code was **slow as hell**
2. I checked `.claude.json` → **17 MB** 😱
3. I opened it → **87 projects** with full chat histories
4. I tried to clean it manually → **JSON hell**
5. I built this tool → **30 seconds later, 732 KB** ✨

**If this saved you time, star the repo! ⭐**

It helps others discover the tool and validates my late-night coding session.

---

## 🗺️ Roadmap

- [ ] Search/filter in Raw JSON view
- [ ] Edit MCP server parameters inline (args, env, cwd)
- [ ] Import project history from JSON
- [ ] Config diff viewer (before/after)
- [ ] Automatic cleanup suggestions (AI-powered?)
- [ ] Export config as shareable template

**Got ideas?** Open an issue!

---

## 🌟 Star History

If you found this useful, **star the repo**! It helps others discover it.

<p align="center">
  <a href="https://star-history.com/#gagarinyury/claude-config-editor&Date">
    <img src="https://api.star-history.com/svg?repos=gagarinyury/claude-config-editor&type=Date" alt="Star History Chart">
  </a>
</p>

---

## 💬 Support

- 🐛 **Bugs:** [Open an issue](https://github.com/gagarinyury/claude-config-editor/issues)
- 💡 **Ideas:** [Open an issue](https://github.com/gagarinyury/claude-config-editor/issues)
- 💬 **Questions:** [Discussions](https://github.com/gagarinyury/claude-config-editor/discussions)
- ⭐ **Show love:** Star the repo!

---

<p align="center">
  <strong>Made with ❤️ and Claude Code</strong><br>
  <sub>(This tool was built using Claude Code. Meta, I know.)</sub>
</p>

<p align="center">
  <strong>If this saved you time, <a href="https://github.com/gagarinyury/claude-config-editor">⭐ star the repo</a>!</strong><br>
  <sub>It takes 2 seconds and makes my day.</sub>
</p>

---

<p align="center">
  <sub>P.S. Your config is probably bloated right now. Go check. I'll wait.</sub>
</p>
