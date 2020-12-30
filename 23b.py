from time import time

MOVES = 10_000_000
CUP_LIMIT = 1_000_000

index_to_node = {}

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"[Node {self.value}]"

    @classmethod
    def from_list(cls, original):
        value = original[0]
        start = current = Node(value)
        index_to_node[value] = current
        for i in range(1, len(original)):
            value = original[i]
            new_node = Node(value)
            index_to_node[value] = new_node
            current.next = new_node
            current = new_node
        return start

    def to_array(self):
        current = self
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

with open("23.txt") as file_obj:
    text = file_obj.read().strip()
    cups = [int(n) for n in list(text)]

current_cup = max(cups) + 1
for _ in range(CUP_LIMIT - len(cups)):
    cups.append(current_cup)
    current_cup += 1

head = Node.from_list(cups)

seen = set()
current = head

def get_next_value(value, taken):
    value -= 1

    while True:
        if value == 0:
            value = CUP_LIMIT
        if any(value == cup.value for cup in taken):
            value -= 1
            continue
        break
    return value


for move in range(MOVES):
    value = current.value

    taken1 = current.next or head
    taken2 = taken1.next or head
    taken3 = taken2.next or head

    if head in [taken1, taken2, taken3]:
        head = taken3.next

    try:
        current.next = current.next.next.next.next
    except AttributeError:
        current.next = None

    dest_value = get_next_value(value, [taken1, taken2, taken3])
    destination = index_to_node[dest_value]
    taken3.next = destination.next
    taken2.next = taken3
    taken1.next = taken2
    destination.next = taken1
    
    current = current.next or head

one_node = index_to_node[1]
next1 = one_node.next
next2 = next1.next

print(next1.value * next2.value)
