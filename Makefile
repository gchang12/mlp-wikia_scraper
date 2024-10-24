VENV_NAME = .venv-mlp_scraper/

_: $(VENV_NAME)
	python3 appearance_counter.py;
$(VENV_NAME):
	python3 -m venv $(VENV_NAME);
	. $(VENV_NAME)/bin/activate;
	pip install -r requirements.txt;
