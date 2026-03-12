# Makefile for convenience, (doesn't look for command outputs)
.PHONY: all
all: {{ cookiecutter.project_slug }}

# Setting environment variables from .env file
# "-" == "if exists" , do not forget to copy .env.template to .env
-include .env

.PHONY: {{ cookiecutter.project_slug }}
{{ cookiecutter.project_slug }} : conda-lock apt docker

conda-lock:
	cd {{ cookiecutter.project_slug }} ; \
	conda-lock lock -f environment.yml -f ../.base_layer/base-notebook-environment.yml  {{ "-f ../.base_layer/pangeo-notebook-environment.yml" if cookiecutter.use_pangeo_notebook }} {{ "-f ../.base_layer/pytorch-notebook-environment.yml" if cookiecutter.use_pytorch_notebook }} -p linux-64  --no-mamba; \
	conda-lock render -k explicit -p linux-64; \
	../generate-packages-list.py conda-linux-64.lock > packages.txt

apt:
	cd {{ cookiecutter.project_slug }} ; \
	../merge-apt.sh ../.base_layer/base-notebook-apt.txt apt.txt {{ "../.base_layer/pangeo-notebook-apt.txt" if cookiecutter.use_pangeo_notebook }} {{ "../.base_layer/pytorch-notebook-apt.txt" if cookiecutter.use_pytorch_notebook }} apt.txt

docker:
	docker build -t cnes/{{ cookiecutter.project_slug }}:master . --progress=plain --platform linux/amd64; \
	docker run -w $(TESTDIR) -v $(PWD):$(TESTDIR) cnes/{{ cookiecutter.project_slug }}:master ./run_tests.sh {{ cookiecutter.project_slug }}


update:
	python update_base_layer.py