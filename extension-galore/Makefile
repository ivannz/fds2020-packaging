# a toy makefile

dttm := $(shell /bin/date "+%Y%m%d-%H%M%S")

wheel:
	@python setup.py bdist_wheel

clean:
	@rm -rf build dist ./arc_*.tar.gz

arc: clean
	tar -zcf ./arc_$(dttm).tar.gz ./*
