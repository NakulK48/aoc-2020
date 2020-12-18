from enum import Enum

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
    while position < len(statement):
        current = statement[position]
        if current == ")":
            return (result, position + 1)
        elif current == "(":
            inner_result, position = evaluate(statement, position + 1)
            result = update(result, inner_result, operation)
            continue
        
        if current == "+":
            operation = Operation.ADD
        elif current == "*":
            operation = Operation.MULT
        else:
            number = int(current)
            result = update(result, number, operation)

        position += 1

    return result, len(statement)

result = sum(evaluate(statement)[0] for statement in lines) 
print(result)