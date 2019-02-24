IMAGE_NAME:=epl_translator
CONTAINER_NAME:=epl_translator
CONTAINER_INSTANCE:=default
PORT:=8000

install:
	python -m pip install -r requirements.txt

build:
	docker build -f Dockerfile -t $(IMAGE_NAME) .

run:
	docker run --rm -d --name $(CONTAINER_NAME) -p=0.0.0.0:$(PORT):$(PORT) $(IMAGE_NAME)

run_locally:
	python ./translator_app/app.py

restart:
	docker stop $(CONTAINER_NAME)
	make run

stop:
	docker stop $(CONTAINER_NAME)

mypy:
	# requiere mypy package installed
	mypy --ignore-missing-imports translator_app && echo "ok"

tests:
	python -m pytest -s -x --tb=short tests

.DEFAULT_GOAL := help


.PHONY: build start test tests install run run_locally restart stop mypy