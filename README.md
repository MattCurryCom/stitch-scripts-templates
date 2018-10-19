# Stitch Scripts templates

## Installation

Requirements:

- Python (>=3.4)
- [poetry](https://github.com/sdispater/poetry)

```bash
# pyenv local 3.x.x
make install
```

## Usage

### Running the notebook server to view and edit templates

This command will start a Jupyter notebook server running on port 8888:

```bash
make serve
```

### Updating the front matter

The `bare` and `minimal_*` templates include a single markdown cell of Scripts info / instructions (herein referred to as the "front matter").

To update the front matter markdown:

1. Start a notebook server: `make serve`
2. Navigate to `bare/template.ipynb` within the Jupyter file tree
3. Make the desired modifications and save the notebook
4. Run `make update_front_matter` to broadcast these changes to the other templates that have front matter
