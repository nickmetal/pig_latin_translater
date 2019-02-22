IMAGE_NAME:=epl_translator
CONTAINER_NAME:=epl_translator
CONTAINER_INSTANCE:=default
PORT:=8000

install:
	python3.7 -m pip install -r requirements.txt

build:
	docker build -f Dockerfile -t $(IMAGE_NAME) .

run:
	docker run --rm -d --name $(CONTAINER_NAME) -p=0.0.0.0:$(PORT):$(PORT) $(IMAGE_NAME)

run_locally:
	python3.7 ./translator_app/app.py

restart:
	docker stop $(CONTAINER_NAME)
	make run

stop:
	docker stop $(CONTAINER_NAME)

tests:
	python3.7 -m mypy --ignore-missing-imports translator_app

.DEFAULT_GOAL := help


.PHONY: build start test tests install run run_locally restart stop