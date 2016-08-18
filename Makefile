#!/bin/bash
#!/bin/env python3

all: horiztemp.pdf out.txt
	
horiztemp.pdf: firsttry.py
	python firsttry.py

out.txt: in.txt
	rm -f out.txt
	for i in {1..100};\
		do cat<in.txt>>out.txt;\
	done
