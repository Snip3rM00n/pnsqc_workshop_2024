lock:
	poetry lock

install-deps-poetry:
	poetry install

install-deps-pip:
	python3 -m pip install -r requirements.txt
