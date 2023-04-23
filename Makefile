init:
	pyenv install 3.10.10
	pyenv exec pip install poetry
	pyenv exec poetry install

shell:
	pyenv exec poetry shell
