with open("14.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

MASK_LENGTH = 36

def padded_binary(original, length):
    stripped = bin(int(original))[2:]  # get rid of 0b
    pad_length = length - len(stripped)
    pad = "0" * pad_length
    return pad + stripped

def apply_mask(value, mask):
    bin_value = padded_binary(value, MASK_LENGTH)
    digits = []
    for value_digit, mask_digit in zip(bin_value, mask):
        next_digit = value_digit if mask_digit == "X" else mask_digit
        digits.append(next_digit)
    return int("".join(digits), 2)

mask = None
memory = {}

for line in lines:
    variable, value = line.split(" = ")
    if variable == "mask":
        mask = value
        continue
    
    memory[variable] = apply_mask(value, mask)

print(sum(memory.values()))
