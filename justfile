install:
    uv tool install -e .

format:
    - uvx ruff check --fix apple_notes
    - uvx ruff format apple_notes

test:
    uvx pytest