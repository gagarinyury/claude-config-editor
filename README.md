# Claude Config Editor

Web-based editor for Claude Code's `.claude.json` configuration file.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

## Features

- 📊 **Overview** - Quick stats and health analysis of your config
- 📁 **Project History** - Manage and clean up project history (the biggest space consumer)
  - Export individual project histories to JSON
  - Bulk delete old/unused projects
  - Sort and search projects by size
- 🔌 **MCP Servers** - View, add, and remove MCP server configurations
- 📝 **Raw JSON** - View and copy the entire config as JSON

## Why?

The `.claude.json` file can grow to **10+ MB** due to project history accumulation. This tool helps you:
- Identify which projects are taking up space
- Clean up old project histories you don't need
- Export specific project histories before deletion
- Manage MCP server configurations visually

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/claude-config-editor.git
cd claude-config-editor

# Run the server (requires Python 3.7+, no dependencies needed)
python3 server.py

# Open your browser
open http://localhost:8765
```

That's it! No installation, no dependencies.

## Usage

### Managing Project History

1. Go to the **"Project History"** tab
2. Click **"Top 10 Largest"** to select the biggest projects
3. Review the selected projects
4. Click **"Delete Selected"** to remove them
5. Click **"💾 Save Changes"** to apply

**Tip:** You can export a project's history before deleting it using the **"💾 Export"** button.

### Managing MCP Servers

1. Go to the **"🔌 MCP Servers"** tab
2. View all configured MCP servers
3. Click **"Delete"** to remove a server
4. Click **"+ Add Server"** to add a new one
5. Click **"💾 Save Changes"** to apply

### Backup

Always create a backup before making changes:
- Click **"📦 Backup"** in the top bar
- The original `.claude.json` is automatically backed up to `.claude.json.backup` when you save

## Configuration File Location

The editor automatically finds your config at:
- macOS/Linux: `~/.claude.json`
- Windows: `%USERPROFILE%\.claude.json`

## Requirements

- Python 3.7 or higher (uses only standard library)
- Claude Code installed and configured

## How It Works

1. Starts a local web server on port 8765
2. Loads `~/.claude.json` via REST API
3. Provides a web interface to edit the config
4. Saves changes back to `~/.claude.json`
5. Creates automatic backups

## FAQ

**Q: Is it safe to delete project history?**
A: Yes. Project history only stores your conversation history. Deleting it won't affect Claude Code functionality, MCP servers, or other settings.

**Q: Will this affect my MCP servers?**
A: No, unless you explicitly delete them in the MCP Servers tab. The tool only modifies what you tell it to.

**Q: Do I need to restart Claude Code after making changes?**
A: Yes, restart Claude Code for changes to take effect.

**Q: What if something goes wrong?**
A: The tool automatically creates a backup at `.claude.json.backup` before saving. You can manually restore it if needed.

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author

Created to solve the problem of Claude Code's config file growing too large due to project history accumulation.
