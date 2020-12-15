with open("15.txt") as file_obj:
    text = file_obj.read().strip()
    first_numbers = [int(entry) for entry in text.split(",")]

last_seen = {}

for index, number in enumerate(first_numbers[:-1]):
    last_seen[number] = index + 1

current = first_numbers[-1]

for turn in range(len(first_numbers), 2020):
    last_index = last_seen.get(current, turn)
    last_seen[current] = turn
    current = turn - last_index

print(current)
