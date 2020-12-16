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
        
def get_target():
    for i in range(PREAMBLE_LENGTH, len(numbers)):
        new_number = numbers[i]
        all_sums = set.union(*num_to_sums.values())
        if new_number not in all_sums:
            return new_number

        oldest_key = next(iter(num_to_sums))
        num_to_sums.pop(oldest_key)
        for old_number, num_sums in num_to_sums.items():
            num_sums.add(new_number + old_number)
        num_to_sums[new_number] = set()
    raise ValueError("No target found")

target = get_target()

lower = 0
upper = 1
sequence_sum = numbers[0] + numbers[1]

while True:
    if sequence_sum == target:
        sequence = numbers[lower:upper+1]
        smallest, largest = min(sequence), max(sequence)
        print(smallest + largest)
        break

    if sequence_sum < target:
        upper += 1
        sequence_sum += numbers[upper]
    else:
        sequence_sum -= numbers[lower]
        lower += 1
