with open("8.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

index = 0
accumulator = 0
visited = set()

while True:
    if index in visited:
        break
    visited.add(index)
    line = lines[index]
    command, number = line.split()
    number = int(number)
    if command == "jmp":
        index += number
        continue
    if command == "acc":
        accumulator += number
    index += 1

print(accumulator)