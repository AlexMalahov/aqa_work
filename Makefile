ifneq ("$(wildcard .env)","")
	include .env
	export
	endif

codegen:
	playwright codegen $(BASE_URL)

tests:
	pytest .

format:
	ruff check --fix . && ruff format 