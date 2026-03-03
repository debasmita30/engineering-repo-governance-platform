install:
	pip install black flake8 pytest pre-commit

lint:
	flake8 .

format:
	black .

test:
	pytest

ci:
	black --check .
	flake8 .
	pytest