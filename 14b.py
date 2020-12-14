with open("14.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

MASK_LENGTH = 36

def padded_binary(original, length):
    stripped = bin(int(original))[2:]  # get rid of 0b
    pad_length = length - len(stripped)
    pad = "0" * pad_length
    return pad + stripped

def apply_mask(address, mask):
    bin_address = padded_binary(address, MASK_LENGTH)
    addresses = [[]]
    for address_bit, mask_bit in zip(bin_address, mask):
        if mask_bit == "0":
            for address in addresses:
                address.append(address_bit)
        elif mask_bit == "1":
            for address in addresses:
                address.append("1")
        else:
            new_addresses = []
            for address in addresses:
                address_copy = address[:]
                address.append("0")
                address_copy.append("1")
                new_addresses.append(address_copy)
            addresses += new_addresses

    return [int("".join(address), 2) for address in addresses]

ADDRESS_START = len("mem[")

mask = None
memory = {}

for line in lines:
    variable, value = line.split(" = ")
    if variable == "mask":
        mask = value
        continue
    base_address = variable[ADDRESS_START:-1]  # remove mem[ and ]
    all_addresses = apply_mask(base_address, mask)
    for address in all_addresses:
        memory[address] = int(value)

print(sum(memory.values()))
