.PHONY: clean dist upload release

TWINE_SIGN_WITH ?= gpg

default:
	echo 'Please choose the Makefile target'

clean:
	rm -rf build dist

dist:
	python setup.py sdist bdist_wheel

upload:
	twine check dist/*
	twine upload --sign --sign-with=$(TWINE_SIGN_WITH) --skip-existing dist/*

release: clean dist upload
