from apple_notes import apple_script
from apple_notes.model import Note


def get_note(title: str) -> str:
    return apple_script.tell_notes_application(f"""
        set theNote to first note whose name is "{title}"
        return the body of theNote
    """)


def get_notes_in_folder(folder_name: str) -> list[Note]:
    script_output = apple_script.tell_notes_application(f"""
        tell folder "{folder_name}" of account "iCloud"
            set output to ""
            repeat with n in notes
                set output to output & name of n & linefeed
            end repeat
            return output
        end tell
    """)
    return [Note(title=title) for title in script_output.split("\n") if title]


def create_note(title: str, body: str, folder: str = "Notes") -> str:
    title_escaped = title.replace('"', '\\"')
    body_escaped = body.replace('"', '\\"')

    full_body = f"""
        <div><b><span style=\\"font-size: 20px\\">{title}</span></b></div>
        {body_escaped}
    """.strip()

    return apple_script.tell_notes_application(f"""
        tell account "iCloud"
            set newNote to make new note at folder "{folder}" with properties {{name: "{title_escaped}", body: ""}}
            -- Now clear the body
            set body of newNote to "{full_body}"
        end tell
    """)


def delete_note(title: str) -> str:
    return apple_script.tell_notes_application(f"""
        tell account "iCloud"
            delete note "{title}"
        end tell
    """)


def create_folder(name: str) -> str:
    return apple_script.tell_notes_application(f"""
        tell account "iCloud"
            make new folder with properties {{name: "{name}"}}
        end tell
    """)


def delete_folder(name: str) -> str:
    return apple_script.tell_notes_application(f"""
        tell account "iCloud"
            delete folder "{name}"
        end tell
    """)


def open_note(note_title: str) -> str:
    return apple_script.tell_notes_application(f"""
        set theNote to first note whose name is "{note_title}"
        activate
        show theNote
    """)
