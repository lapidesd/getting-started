#!/bin/bash

out.txt: in.txt
	rm -f out.txt
	for i in {1..100};\
		do cat<in.txt>>out.txt;\
	done