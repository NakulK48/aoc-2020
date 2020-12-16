with open("16.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

class Rule:
    def __init__(self, rule_line):
        self.field, ranges_str = rule_line.split(": ")
        range_strings = ranges_str.split(" or ")
        self.ranges = []
        for range_string in range_strings:
            bottom, top = range_string.split("-")
            self.ranges.append(range(int(bottom), int(top) + 1))
    
    def validate(self, value):
        return any(value in this_range for this_range in self.ranges)

first_blank = lines.index("")
rule_lines = lines[:first_blank]

my_ticket_label = lines.index("your ticket:")
my_ticket_line = lines[my_ticket_label + 1]

nearby_start = lines.index("nearby tickets:")
nearby_ticket_lines = lines[nearby_start + 1:]

def parse_ticket_line(ticket_line):
    return [int(x) for x in ticket_line.split(",")]

my_ticket = parse_ticket_line(my_ticket_line)

rules = [Rule(line) for line in rule_lines]
rules_dict = {rule.field: rule for rule in rules}

valid_tickets = [my_ticket]
for ticket_line in nearby_ticket_lines:
    ticket_numbers = parse_ticket_line(ticket_line)
    for number in ticket_numbers:
        if not any(rule.validate(number) for rule in rules):
            break
    else:
        valid_tickets.append(ticket_numbers)

possible_names_by_field = [set(rules_dict.keys()) for _ in rules_dict]

for ticket in valid_tickets:
    for field_index, field_value in enumerate(ticket):
        remaining_rule_names = possible_names_by_field[field_index]
        new_rule_names = {
            name for name in remaining_rule_names if rules_dict[name].validate(field_value)
        }
        possible_names_by_field[field_index] = new_rule_names

confirmed_names_by_field = [None for _ in possible_names_by_field]

while any(possible_names_by_field):
    for index, field_name_set in enumerate(possible_names_by_field):
        if len(field_name_set) == 1:
            field_name = next(iter(field_name_set))
            confirmed_names_by_field[index] = field_name
            for entry in possible_names_by_field:
                entry.discard(field_name)

result = 1
for field_index, field_value in enumerate(my_ticket):
    if confirmed_names_by_field[field_index].startswith("departure"):
        result *= field_value

print(result)
