mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))

test:
	cd simulator && python -m pytest\
	&& cd ../recengine && python -m pytest
