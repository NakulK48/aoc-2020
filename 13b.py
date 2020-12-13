import math

with open("13.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

bus_offsets = lines[1].split(",")

def get_modulo(bus_str, offset):
    bus = int(bus_str)
    modulo = bus - (offset % bus)
    return (bus, 0 if modulo == bus else modulo)

modulos = [
    get_modulo(bus, offset) for offset, bus in enumerate(bus_offsets) if bus != "x"
]

modulos.sort(reverse=True)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

to_add, current = modulos[0]

for bus, modulo in modulos[1:]:
    while True:
        if (current % bus) == modulo:
            to_add = lcm(to_add, bus)
            break
        current += to_add

print(current)
