with open("10.txt") as file_obj:
    lines = [int(line.strip()) for line in file_obj.readlines()]

lines.sort()

one_jolt = 0
three_jolt = 1  # Include the final jump to the phone

prev = 0
for adapter in lines:
    diff = adapter - prev
    if diff == 1:
        one_jolt += 1
    elif diff == 3:
        three_jolt += 1

    prev = adapter 

print(one_jolt * three_jolt)