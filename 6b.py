with open("6.txt") as file_obj:
    groups = file_obj.read().split("\n\n")

total = 0

for group in groups:
    people = group.split("\n")
    yesses = set(people[0])
    for person in people:
        yesses.intersection_update(set(person))
    total += len(yesses)

print(total)