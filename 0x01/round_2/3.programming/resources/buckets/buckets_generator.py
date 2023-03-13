#!/usr/bin/python3
import random

with open("buckets-sample.txt", "w") as fio_buckets:
    for i in range(20):
        match random.randrange(5):
            case 0:
                fio_buckets.write("alice\n")
            case 1:
                fio_buckets.write("billy\n")
            case 2:
                fio_buckets.write("charlie\n")
            case 3:
                fio_buckets.write("danny\n")
            case 4:
                fio_buckets.write("elise\n")

with open("buckets.txt", "w") as fio_buckets:
    for i in range(5000):
        match random.randrange(5):
            case 0:
                fio_buckets.write("alice\n")
            case 1:
                fio_buckets.write("billy\n")
            case 2:
                fio_buckets.write("charlie\n")
            case 3:
                fio_buckets.write("danny\n")
            case 4:
                fio_buckets.write("elise\n")

