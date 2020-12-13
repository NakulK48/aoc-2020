import math

with open("13.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

bus_offsets = lines[1].split(",")

bus_to_offset = {index: int(bus) for index, bus in enumerate(bus_offsets) if bus != "x"}

modulos = []

for offset, bus in bus_to_offset.items():
    modulo = bus - (offset % bus)
    if modulo == bus:
        modulo = 0
    modulos.append((bus, modulo))

modulos.sort(reverse=True)

to_add, current = modulos[0]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for bus, modulo in modulos[1:]:
    while True:
        if (current % bus) == modulo:
            to_add = lcm(to_add, bus)
            break
        current += to_add

print(current)
