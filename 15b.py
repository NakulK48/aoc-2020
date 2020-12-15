with open("15.txt") as file_obj:
    entries = file_obj.read().strip().split(",")
    first_numbers = [int(entry) for entry in entries]

last_seen = {}

for index, number in enumerate(first_numbers[:-1]):
    last_seen[number] = index + 1

current = first_numbers[-1]

for turn in range(len(first_numbers), 30000000):
    last_index = last_seen.get(current)
    if last_index is None:
        next_number = 0
    else:
        next_number = turn - last_index
    last_seen[current] = turn
    current = next_number

print(current)
