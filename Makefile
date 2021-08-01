install:
	pip install -e .['dev']
dev:
	uvicorn msgls.main:app --reload