from enum import Enum
from collections import deque

with open("18.txt") as file_obj:
    lines = [line.strip().replace(" ", "") for line in file_obj.readlines()]

class Operation(Enum):
    ADD = 0
    MULT = 1

def update(old_result, new_number, operation):
    if operation == Operation.ADD:
        return old_result + new_number
    if operation == Operation.MULT:
        return old_result * new_number
    raise ValueError(f"Invalid operation {operation}")

def evaluate(statement, start_pos=0):
    position = start_pos
    result = 0
    operation = Operation.ADD
    stack = deque()
    while position < len(statement):
        current = statement[position]
        if current == ")":
            while stack:
                result *= stack.pop()
            return (result, position + 1)
        elif current == "(":
            inner_result, position = evaluate(statement, position + 1)
            result = update(result, inner_result, operation)
            continue
        if current == "*":
            stack.append(result)
            result = 0
            operation = Operation.ADD
            
        elif current == "+":
            operation = Operation.ADD
        else:
            number = int(current)
            result = update(result, number, operation)

        position += 1

    while stack:
        result *= stack.pop()
    return result, len(statement)

cases = [
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 46),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    ("((2+4*9)*(6+9*8+6)+6)+2+4*2", 23340),
    ("(2 + 4 * 9)", 54),
    ("(6 + 9 * 8 + 6)", 210),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)", 11664)
]

for statement, result in cases:
    statement = statement.replace(" ", "")
    actual, _ = evaluate(statement)
    if actual != result:
        print(f"{statement} failed: result {actual}")

result = sum(evaluate(statement)[0] for statement in lines) 
print(result)