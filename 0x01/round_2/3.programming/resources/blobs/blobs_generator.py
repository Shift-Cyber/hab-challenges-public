#!/usr/bin/python3
import random

with open("blobs-sample.txt", "w") as fio_buckets:
    fio_buckets.write("(52,-31)\n\n")

    for i in range(20):
        match random.randrange(8):
            case 0:
                fio_buckets.write("↑ ")
            case 1:
                fio_buckets.write("↓ ")
            case 2:
                fio_buckets.write("← ")
            case 3:
                fio_buckets.write("→ ")
            case 4:
                fio_buckets.write("↖ ")
            case 5:
                fio_buckets.write("↗ ")
            case 6:
                fio_buckets.write("↘ ")
            case 7:
                fio_buckets.write("↙ ")
    fio_buckets.write("\n")


with open("blobs.txt", "w") as fio_buckets:
    fio_buckets.write("(136,-8891)\n\n")

    for i in range(5000):
        match random.randrange(8):
            case 0:
                fio_buckets.write("↑ ")
            case 1:
                fio_buckets.write("↓ ")
            case 2:
                fio_buckets.write("← ")
            case 3:
                fio_buckets.write("→ ")
            case 4:
                fio_buckets.write("↖ ")
            case 5:
                fio_buckets.write("↗ ")
            case 6:
                fio_buckets.write("↘ ")
            case 7:
                fio_buckets.write("↙ ")
    fio_buckets.write("\n")
