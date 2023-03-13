#!/usr/bin/python3

people = { person : 0 for person in ['alice', 'billy', 'charlie', 'danny', 'elise']}

with open("buckets.txt", "r") as fio_buckets:
    for line in fio_buckets:
        match line.strip():
            case "alice":
                people['alice'] += 1
            case "billy":
                people['billy'] += 1
            case "charlie":
                people['charlie'] += 1
            case "danny":
                people['danny'] += 1
            case "elise":
                people['elise'] += 1

print(f"solution: {people['danny'] * people['elise']}")