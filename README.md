![](logo.png)

# Apple Notes Python API

A Python API to interact with Apple's Notes app.

## Usage

### CLI

Open Note:

```sh
uvx apple-notes open Home
```

### Python API

```python
import apple_notes
```

Open Note:

```python
apple_notes.open_note("Home)
```

## Development

Clone the repository:

```sh
git clone ...
```

Install from repository:

```sh
uv tool install -e .
```

Run the tests:

```sh
uvx pytest
```
