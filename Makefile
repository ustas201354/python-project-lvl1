# Makefile

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

calc:
	poetry run calc

brain-gcd:
	poetry run brain_gcd

brain-progression:
	poetry run brain_progression
