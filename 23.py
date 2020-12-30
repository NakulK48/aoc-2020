MOVES = 100

with open("23.txt") as file_obj:
    text = file_obj.read().strip()
    cups = [int(n) for n in list(text)]

def take_cups(cup_list, index):
    taken_cup_list = (
        cup_list[index + 1 : index + 4]
    )
    start_index = max(0, 3 - len(taken_cup_list))
    taken_cup_list += cup_list[: start_index]
    new_cup_list = (
        cup_list[start_index : index + 1] + cup_list[index + 4 :]
    )
    return new_cup_list, taken_cup_list

def place_cups(cup_list, taken_cups, old_value):
    value = old_value - 1

    while True:
        if value == 0:
            value = max(cup_list)
        try:
            new_index = cup_list.index(value)
            break
        except ValueError: 
            value -= 1

    new_cup_list = (
        cup_list[:new_index + 1]
        + taken_cups
        + cup_list[new_index + 1:]
    )
    return new_cup_list

current_index = 0

for _ in range(MOVES):
    value = cups[current_index]
    new_cup_list, taken_cup_list = take_cups(cups, current_index)
    cups = place_cups(new_cup_list, taken_cup_list, value)
    current_index = cups.index(value) + 1
    if current_index == len(cups):
        current_index = 0

one_index = cups.index(1)
rearranged = cups[one_index + 1 : ] + cups[:one_index]
result = "".join(str(cup) for cup in rearranged)
print(result)