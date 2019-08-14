.PHONY: clean dist upload release

default:
	echo 'Please choose the Makefile target'

clean:
	rm -rf build dist

dist:
	python setup.py sdist bdist_wheel

upload:
	twine check dist/*
	twine upload --skip-existing dist/*

release: clean dist upload
