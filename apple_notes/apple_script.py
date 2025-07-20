import subprocess


def _run_script(script: str) -> str:
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    return result.stdout.strip()


def tell_notes_application(inner_script: str) -> str:
    return _run_script(
        f"""
        tell application "Notes"
            {inner_script}
        end tell
    """.strip()
    )
