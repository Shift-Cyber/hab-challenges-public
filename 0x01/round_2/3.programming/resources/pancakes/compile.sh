#!/usr/bin/bash

for i in $(seq $1 $2);
do
   case $(shuf -i 0-3 -n 1) in
        0)
            mips-linux-gnu-gcc binary.c -o binary_$i -static
            ;;

        1)
            aarch64-linux-gnu-gcc binary.c -o binary_$i -static
            ;;

        2)
            sparc64-linux-gnu-gcc binary.c -o binary_$i -static
            ;;

        3)
            powerpc-linux-gnu-gcc binary.c -o binary_$i -static
            ;;
        esac
done
