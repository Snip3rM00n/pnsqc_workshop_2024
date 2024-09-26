lock:
	poetry lock

install-deps-poetry:
	poetry install

install-deps-pip:
	python3 -m pip install -r requirements.txt

test-workshop:
	python3 -m pytest ./tests/test_workshop.py

test-io:
	python3 -m pytest ./tests/test_io.py

test-all:
	python3 -m pytest ./tests/
