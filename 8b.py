from collections import defaultdict, deque

with open("8.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]


GOAL_INDEX = len(lines)

def parse_line(line):
    command, number = line.split()
    number = int(number)
    return command, number

get_here_from = defaultdict(list)

for index, line in enumerate(lines):
    command, number = parse_line(line)
    if command == "jmp":
        get_here_from[index + number].append(index)
    else:
        get_here_from[index + 1].append(index)
    
visited = {GOAL_INDEX: 0}
candidates = deque([(GOAL_INDEX, 0)])

while candidates:
    index, acc_from_here = candidates.popleft()
    new_acc = acc_from_here
    if index != GOAL_INDEX:
        command, number = parse_line(lines[index])
        if command == "acc":
            new_acc += number
    
    visited[index] = new_acc
    
    for prev_index in get_here_from[index]:
        candidates.append((prev_index, new_acc))

index = accumulator = 0

while True:
    line = lines[index]
    command, number = parse_line(line)
    
    if command == "jmp":
        if (index + 1) in visited:
            accumulator += visited[index + 1]
            print(f"Changed line {index+1} from jmp to nop")
            break
        index += number
        continue
    if command == "acc":
        accumulator += number
    if command == "nop":
        if (index + number) in visited:
            accumulator += visited[index + number]
            print(f"Changed line {index+1} from nop to jmp")
            break
    index += 1

print(accumulator)