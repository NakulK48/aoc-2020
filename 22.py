def parse_section(section):
    lines = section.split("\n")
    del lines[0]
    return [int(x) for x in lines]

with open("22.txt") as file_obj:
    text = file_obj.read()


section1, section2 = text.split("\n\n")
deck1 = parse_section(section1)
deck2 = parse_section(section2)

while deck1 and deck2:
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1 += [card1, card2]
    else:
        deck2 += [card2, card1]

remaining = deck1 or deck2
remaining.reverse()
result = sum((index+1) * card for index, card in enumerate(remaining))
print(result)
