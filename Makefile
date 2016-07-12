.PHONY: help clean install install info server uwsgi


install:
	pip install uwsgi
	pip install -Ur requirements.txt

clean:
	python manage.py clean

lint: clean
	@rm -f violations.flake8.txt
	flake8 --exclude=env --exclude=archive . > violations.flake8.txt

info:
	@uname -a
	@pyenv --version
	@pip --version
	@python --version

server:
	python manage.py server

uwsgi:
	uwsgi --socket 127.0.0.1:5080 --module service --callable application
