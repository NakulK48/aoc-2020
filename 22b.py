def parse_section(section):
    lines = section.split("\n")
    del lines[0]
    return [int(x) for x in lines]

with open("22.txt") as file_obj:
    text = file_obj.read()


section1, section2 = text.split("\n\n")
original_deck1 = parse_section(section1)
original_deck2 = parse_section(section2)

def get_score(deck):
    result = sum((index+1) * card for index, card in enumerate(reversed(deck)))
    return result


def get_key(deck1, deck2):
    return f"{deck1}{deck2}"

def recursive_combat(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        key = get_key(deck1, deck2)
        if key in seen:
            return get_score(deck1), True
        seen.add(key)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deck1[:card1]
            new_deck2 = deck2[:card2]
            _, deck1_wins = recursive_combat(new_deck1, new_deck2)
        else:
            deck1_wins = (card1 > card2)

        if deck1_wins:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    remaining = deck1 or deck2
    return get_score(remaining), (remaining == deck1)

result, _ = recursive_combat(original_deck1, original_deck2)
print(result)
