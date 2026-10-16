# Notes MCP Server

A simple note-taking MCP (Model Context Protocol) server built with [FastMCP](https://github.com/jlowin/fastmcp). It lets any MCP-compatible AI client (Claude Desktop, Cursor, etc.) add, list, search, update, and delete notes stored in a local JSON file, plus read Markdown files from the same folder.

## Features

- **add_note** — add a new note
- **list_notes** — list all saved notes
- **search_notes** — case-insensitive text search across notes
- **update_note** — update a note's text by index
- **delete_note** — delete a note by index
- **read_md** — read a Markdown file from the notes folder

All notes are persisted to `notes.json` in the current working directory. The file is created automatically on first write.

## Requirements

- Python 3.10+
- [FastMCP](https://github.com/jlowin/fastmcp)

## Installation

```bash
git clone https://github.com/<your-username>/notes-mcp.git
cd notes-mcp
pip install fastmcp