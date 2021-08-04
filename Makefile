install:
	pip install pipenv \
	&& pipenv lock -r --dev > requirements.txt \
	&& pip install -r requirements.txt

test:
	python -m pytest -svv --cov=cli --cov-report term-missing