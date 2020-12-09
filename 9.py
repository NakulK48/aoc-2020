from collections import defaultdict

with open("9.txt") as file_obj:
    numbers = [int(line.strip()) for line in file_obj.readlines()]

PREAMBLE_LENGTH = 25
num_to_sums = {}

for i in range(PREAMBLE_LENGTH):
    first = numbers[i]
    num_to_sums[first] = set()
    for j in range(i+1, PREAMBLE_LENGTH):
        second = numbers[j]
        num_to_sums[first].add(first + second)
        
for i in range(PREAMBLE_LENGTH, len(numbers)):
    new_number = numbers[i]
    all_sums = set.union(*num_to_sums.values())
    if new_number not in all_sums:
        print(new_number)
        break

    oldest_key = next(iter(num_to_sums))
    num_to_sums.pop(oldest_key)
    for old_number, num_sums in num_to_sums.items():
        num_sums.add(new_number + old_number)
    num_to_sums[new_number] = set()