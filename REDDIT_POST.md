# Reddit Posts for Claude Config Editor

## For r/ClaudeAI (Main Post)

**Title:** [Tool] I built a GUI to clean up your bloated .claude.json (17 MB → 732 KB in 30 seconds)

**Body:**

Hey everyone! 👋

**TL;DR:** Your `.claude.json` is probably huge (mine was 17 MB). I built a web-based GUI to clean it up in 30 seconds. Zero dependencies, fully local, auto-backup.

🔗 **GitHub:** https://github.com/gagarinyury/claude-config-editor

---

### The Problem I Had

After using Claude Code for a few weeks, I noticed it was getting slower. Checked my `.claude.json` file → **17 MB** 😱

Turns out Claude stores **every conversation from every project**. I had 87 projects with full chat histories eating up disk space.

### What I Built

A simple web interface that lets you:
- 📊 See which projects are taking up space
- 🗑️ Delete old projects in bulk (top 10 = 90% of bloat)
- 💾 Export project histories before deletion (download as JSON)
- 🔌 Manage MCP servers visually (no more JSON editing)
- 🛡️ Auto-backup before every save

### Results

**Before:** 17 MB, 87 projects, slow startup
**After:** 732 KB, 2 active projects, instant startup
**Time:** 30 seconds

### Features

✅ Works with both Claude Code AND Claude Desktop
✅ Auto-detects your config files
✅ Zero dependencies (Python stdlib only)
✅ Fully local (localhost:8765, no internet required)
✅ Auto-backup (can't break anything)

### Quick Start

```bash
git clone https://github.com/gagarinyury/claude-config-editor.git
cd claude-config-editor
python3 server.py
# Opens at http://localhost:8765
```

That's it. No pip install, no npm, no configuration.

### Screenshots

*(Would add screenshots here if you make them)*

### Why This Matters

If your Claude Code has been slow lately, this might be why. The config file grows silently, and there's no built-in way to clean it up.

This tool gives you visibility into what's taking up space and lets you clean it safely.

### Safety

- Auto-backup before every save (`.claude.backup.json`)
- Only modifies what you explicitly delete
- Export any project history before deletion
- Open source (read the code, it's 300 lines)

---

**Questions? Issues? Feature requests?**
GitHub: https://github.com/gagarinyury/claude-config-editor

If this helps you, star the repo! ⭐ It helps others discover it.

---

## For r/Python (Shorter, Code-Focused)

**Title:** [Project] Web-based config editor for Claude Code (Python stdlib only, no dependencies)

**Body:**

Built a simple web-based config editor for Claude Code using only Python's standard library.

**GitHub:** https://github.com/gagarinyury/claude-config-editor

### The Problem
Claude Code stores all conversation history in `~/.claude.json`. After a few weeks, this file can balloon to 10-20 MB, causing slow startup times.

### The Solution
A lightweight HTTP server (Python stdlib) + single-page web UI that lets you:
- Visualize config size by project
- Delete old project histories
- Export specific projects to JSON
- Manage MCP server configurations

### Tech Stack
- Backend: Python `http.server` + `json` + `pathlib` (that's it)
- Frontend: Vanilla JS + CSS (no frameworks)
- Total: ~300 lines Python + ~700 lines HTML/CSS/JS

### Quick Start
```bash
python3 server.py  # No pip install needed
```

### Features I'm Proud Of
- Auto-detects both Claude Code and Claude Desktop configs
- Works cross-platform (macOS, Linux, Windows)
- Auto-backup before every save
- Zero external dependencies

### Why No Dependencies?
Because you shouldn't need Flask/FastAPI/React for a simple local tool. Python's stdlib is powerful enough.

Feedback welcome! Especially on code structure and edge cases I might have missed.

---

## For r/LocalLLaMA (Technical Community)

**Title:** Claude Code config cleanup tool - reduced my config from 17 MB to 732 KB

**Body:**

**Background:** Claude Code stores full conversation history for every project in `~/.claude.json`. No built-in cleanup mechanism exists.

**Problem:** After 3 months of use, my config was 17 MB with 87 projects. Claude Code startup time increased from ~1s to ~5s.

**Solution:** Built a web-based GUI to manage this config file.

🔗 https://github.com/gagarinyury/claude-config-editor

### Technical Details

**Architecture:**
- Python HTTP server (stdlib only)
- REST API (`/api/config`, `/api/save`, `/api/project`)
- Single-page web interface (vanilla JS)
- Auto-detection for both CLI and Desktop configs

**Features:**
- Project size analysis (find bloat)
- Bulk delete with selection
- Individual project export (JSON)
- MCP server management
- Automatic backup before save

**Safety:**
- Non-destructive (read-only by default)
- Atomic writes with backup
- Cross-platform path handling

### Results

| Metric | Before | After |
|--------|--------|-------|
| File size | 17 MB | 732 KB |
| Projects | 87 | 2 |
| Startup time | ~5s | ~1s |

### Use Cases Beyond Claude

The pattern is useful for any tool that accumulates config bloat:
- LLM chat history management
- Local model conversation logs
- Any JSON-based config that grows over time

Code is MIT licensed. PRs welcome.

---

## For r/SideProject (Casual, Story-Focused)

**Title:** Built a tool to fix my slow Claude Code (17 MB config → 732 KB in 30 seconds)

**Body:**

**The frustration:** Claude Code was getting slower every day. Didn't know why.

**The discovery:** Checked `~/.claude.json` → 17 MB 😱

Turns out Claude saves EVERY conversation from EVERY project. I had 87 projects worth of chat history just sitting there.

**The solution:** Built a simple web tool to clean it up.

### What it does:
- Shows which projects are taking up space
- Lets you delete old ones (with export option)
- Manages MCP servers visually
- Auto-backup so you can't break anything

### The result:
**17 MB → 732 KB in 30 seconds**

Claude Code now starts instantly again.

### Tech:
- Python (no dependencies)
- Web interface (runs on localhost)
- Works with both Claude Code and Desktop

### Try it:
```bash
git clone https://github.com/gagarinyury/claude-config-editor.git
cd claude-config-editor
python3 server.py
```

It's free, open source, and takes 30 seconds to clean up months of bloat.

**GitHub:** https://github.com/gagarinyury/claude-config-editor

If your Claude has been slow, this might be why!

---

## Best Practices for Posting

### Timing
- **Best time:** Tuesday-Thursday, 9-11 AM EST
- **Avoid:** Weekends, late night

### Engagement Strategy
1. **Reply to every comment in first 2 hours**
2. **Be helpful, not defensive**
3. **Add value in comments** (tips, troubleshooting)

### Follow-Up Comments to Post
After posting, add a comment with:
- Link to specific features
- Screenshots/GIFs (if you make them)
- "Happy to answer questions!"

### Example Follow-Up Comment:
> OP here! Happy to answer any questions about the tool.
>
> Quick FAQ:
> - **Is it safe?** Yes, auto-backup before every save
> - **Windows support?** Yes, works on macOS/Linux/Windows
> - **Dependencies?** Zero. Python stdlib only
>
> If you try it, let me know how much space you saved! 💾

---

## Subreddits to Post In

### Primary (High Engagement):
1. **r/ClaudeAI** - Main community (~50k members)
2. **r/Python** - For technical audience (~1.5M members)
3. **r/SideProject** - For indie makers (~200k members)

### Secondary (Niche):
4. **r/LocalLLaMA** - Technical LLM users (~150k)
5. **r/commandline** - CLI tool fans (~100k)
6. **r/opensource** - Open source enthusiasts (~200k)

### Wait 24-48 hours between posts to different subs!

---

## Expected Reception

### Positive Comments You'll Get:
- "This is exactly what I needed!"
- "My config was 23 MB, now 1.8 MB. Thank you!"
- "Why isn't this built into Claude?"

### Negative Comments You'll Get:
- "Why not just use jq?" → Answer: "You could, but this is visual and safer"
- "Seems risky" → Answer: "Auto-backup + open source, check the code"
- "I don't have this problem" → Answer: "Lucky you! Others do."

### How to Respond:
- Be grateful for positive feedback
- Be patient with skeptics (they'll convert)
- Never argue, just add value

---

## Post-Launch Checklist

After posting:
- [ ] Reply to comments within 1 hour
- [ ] Update README if people ask questions
- [ ] Screenshot highly-upvoted comments for social proof
- [ ] Cross-post to other communities (wait 24h)
- [ ] Track stars on GitHub (celebrate milestones!)

Good luck! 🚀
