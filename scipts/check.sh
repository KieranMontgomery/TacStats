#!/bin/bash

poetry run black --check --diff . &&
poetry run flake8 src/ tests/ && 
poetry run isort . -c &&
poetry run pytest
