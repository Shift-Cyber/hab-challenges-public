DEPS=binary.c

binarymake: binary.c
	bash compile.sh 0 17
	gcc binary.c -o binary_18 -static
	bash compile.sh 19 22
	gcc binary.c -o binary_23 -static
	bash compile.sh 24 50

	zip pancakes.zip binary_*
	rm binary_*

clean:
	rm pancakes.zip
	rm binary_*