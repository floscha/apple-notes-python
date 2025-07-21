install:
    uv tool install -e .

format:
    pre-commit run --all-files

test *args:
    uvx pytest {{ args }}