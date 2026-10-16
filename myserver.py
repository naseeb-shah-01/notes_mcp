from fastmcp import FastMCP
from pathlib import Path
import json

BASE = Path.cwd()
NOTES_FILE = BASE / "notes.json"

mcp = FastMCP(
    name="Notes",
    instructions="This is a simple note-taking application using FastMCP."
)


def load_notes() -> list[dict]:
    if not NOTES_FILE.exists():
        return []
    try:
        return json.loads(NOTES_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_notes(notes: list[dict]) -> None:
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    NOTES_FILE.write_text(
        json.dumps(notes, indent=4),
        encoding="utf-8",
    )


@mcp.tool(name="add_note", description="Add a new note.")
def add_note(note: str) -> dict:
    notes = load_notes()
    entry = {"note": note}
    notes.append(entry)
    save_notes(notes)
    return {"message": "Note added.", "note": entry}


@mcp.tool(name="list_notes", description="List all notes.")
def list_notes() -> list[dict]:
    return load_notes()


@mcp.tool(name="delete_note", description="Delete a note by its index.")
def delete_note(index: int) -> dict:
    notes = load_notes()
    if index < 0 or index >= len(notes):
        return {"error": "Note not found."}
    removed = notes.pop(index)
    save_notes(notes)
    return {"message": "Note deleted.", "deleted": removed, "notes": notes}


@mcp.tool(name="search_notes", description="Search notes by text (case-insensitive).")
def search_notes(query: str) -> list[dict]:
    q = query.lower()
    results = []
    for i, note in enumerate(load_notes()):
        if q in note.get("note", "").lower():
            results.append({"index": i, "note": note["note"]})
    return results


@mcp.tool(name="update_note", description="Update a note's text by its index.")
def update_note(index: int, new_text: str) -> dict:
    notes = load_notes()
    if index < 0 or index >= len(notes):
        return {"error": "Note not found."}
    old = notes[index]["note"]
    notes[index]["note"] = new_text
    save_notes(notes)
    return {
        "message": "Note updated.",
        "index": index,
        "old": old,
        "new": new_text,
    }




if __name__ == "__main__":
    mcp.run()