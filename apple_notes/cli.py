import sys

from apple_notes import api


def run(args: list[str]) -> None:
    match args:
        case []:
            print("Error: No command was provided.")
        case "get", "note", title:
            print(api.get_note(title))
        case "list", "notes", folder_name:
            print(api.get_notes_in_folder(folder_name))
        case "create", "note", title, text:
            api.create_note(title, text)
        case "create", "note", title:
            # Allow piping text to CLI command. End with ctrl + d
            text: list[str] = []
            for line in sys.stdin:
                if line:  # Only process non-empty lines.
                    text.append(line.strip())
            api.create_note(title, "\n".join(text))
        case "delete", "note", title:
            api.delete_note(title)
        case "create", "folder", folder_name:
            api.create_folder(folder_name)
        case "delete", "folder", folder_name:
            api.delete_folder(folder_name)
        case "open", note_name:
            api.open_note(note_name)
        case _:
            print(f"Error: Command {args!r} is not supported.")
