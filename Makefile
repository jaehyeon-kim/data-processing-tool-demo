install:
	pip install pipenv \
	&& pipenv lock -r --dev > requirements.txt \
	&& pip install -r requirements.txt

format:
	black *.py --line-length 100

test:
	python -m pytest -svv --cov=hello test_hello.py