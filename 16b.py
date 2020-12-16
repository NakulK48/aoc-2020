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

def get_relevant_lines():
    first_blank = lines.index("")
    rule_lines = lines[:first_blank]

    my_ticket_label = lines.index("your ticket:")
    my_ticket_line = lines[my_ticket_label + 1]

    nearby_start = lines.index("nearby tickets:")
    nearby_ticket_lines = lines[nearby_start + 1:]

    return rule_lines, my_ticket_line, nearby_ticket_lines

def parse_ticket_line(ticket_line):
    return [int(x) for x in ticket_line.split(",")]

def get_valid_tickets(ticket_lines, rules):
    valid_tickets = [my_ticket]
    for ticket_line in nearby_ticket_lines:
        ticket_numbers = parse_ticket_line(ticket_line)
        for number in ticket_numbers:
            if not any(rule.validate(number) for rule in rules):
                break
        else:
            valid_tickets.append(ticket_numbers)
    return valid_tickets

def get_valid_names_by_field(rules, tickets):
    rules_dict = {rule.field: rule for rule in rules}
    possible_names_by_field = [set(rules_dict.keys()) for _ in rules_dict]

    for ticket in valid_tickets:
        for field_index, field_value in enumerate(ticket):
            remaining_rule_names = possible_names_by_field[field_index]
            new_rule_names = {
                name for name in remaining_rule_names if rules_dict[name].validate(field_value)
            }
            possible_names_by_field[field_index] = new_rule_names
    
    return possible_names_by_field

def solve_for_field_names(names_by_field):
    confirmed_names_by_field = [None for _ in valid_names_by_field]

    while any(valid_names_by_field):
        for index, field_name_set in enumerate(valid_names_by_field):
            if len(field_name_set) == 1:
                field_name = next(iter(field_name_set))
                confirmed_names_by_field[index] = field_name
                for entry in valid_names_by_field:
                    entry.discard(field_name)
    
    return confirmed_names_by_field

rule_lines, my_ticket_line, nearby_ticket_lines = get_relevant_lines()
my_ticket = parse_ticket_line(my_ticket_line)

rules = [Rule(line) for line in rule_lines]
valid_tickets = get_valid_tickets(nearby_ticket_lines, rules)
valid_tickets.append(my_ticket)

valid_names_by_field = get_valid_names_by_field(rules, valid_tickets)
names_by_field = solve_for_field_names(valid_names_by_field)

result = 1
for field_index, field_value in enumerate(my_ticket):
    if names_by_field[field_index].startswith("departure"):
        result *= field_value

print(result)
