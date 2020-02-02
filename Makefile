setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.venv
	# afterward then source
    source ~/.venv/bin/activate

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py