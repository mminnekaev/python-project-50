install:
	poetry install

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest

check-coverage:
	poetry run pytest --cov
