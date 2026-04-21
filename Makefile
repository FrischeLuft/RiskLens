.PHONY: install test lint format run

install:
	python3 -m pip install -e ".[dev]"

test:
	python3 -m unittest discover -s tests -v

lint:
	ruff check src tests

format:
	ruff check src tests --fix

run:
	python3 -m risklens.cli
