pytest: Makefile
	python3 -m pytest -x

docu: Makefile
	cd doc/rtd && make html

docu-autobuild: Makefile
	cd doc/rtd && make autobuild
