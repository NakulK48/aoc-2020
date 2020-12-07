with open("6.txt") as file_obj:
    groups = [group.replace("\n", "") for group in file_obj.read().split("\n\n")]

total = sum(len(set(group)) for group in groups)
print(total)
