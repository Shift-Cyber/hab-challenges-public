#!/usr/bin/python3
import re

file_name = "blobs.txt"

with open(file_name, "r") as fio_blobs:
    x,y = re.findall("-?[0-9]\d*", fio_blobs.readlines()[0])
    x,y = int(x),int(y)

    print(f"Starting position: {x} {y}")


with open(file_name, "r") as fio_blobs:
    for c in fio_blobs.readlines()[2].split(" "):
        match c:
            case "↑":
                y += 1
            case "↓":
                y -= 1
            case "←":
                x -= 1
            case "→":
                x += 1
            case "↖":
                x -= 1
                y += 1
            case "↗":
                x += 1
                y += 1
            case "↘":
                x += 1
                y -= 1
            case "↙":
                x -= 1
                y -= 1

    print(f"Ending position: {x} {y}")

print(f"\nSolution: {x*y}")