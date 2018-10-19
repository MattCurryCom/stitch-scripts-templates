install:
	poetry install

serve:
	poetry run jupyter notebook --notebook-dir templates/

update_front_matter:
	poetry run python update-front-matter.py

clear_notebook_metadata:
	poetry run python clear-notebook-metadata.py
