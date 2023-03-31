VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate

.PHONY: all install clean

all: install

install: $(VENV_NAME)/bin/activate
	$(VENV_ACTIVATE) && \
	pip install -r requirements.txt

clean:
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete

run: $(VENV_NAME)/bin/activate
	$(VENV_ACTIVATE) && \
	python api.py

test: $(VENV_NAME)/bin/activate
	$(VENV_ACTIVATE) && \
	python -m unittest discover -v

# build virtual environment
$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
