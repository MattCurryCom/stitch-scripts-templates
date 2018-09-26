install:
	pipenv install

serve:
	pipenv run jupyter notebook --notebook-dir templates/

update_front_matter:
	pipenv run python update-front-matter.py

clear_notebook_metadata:
	pipenv run python clear-notebook-metadata.py
