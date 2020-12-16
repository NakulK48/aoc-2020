with open("16.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]
    
first_blank = lines.index("")
rule_lines = lines[:first_blank]

nearby_start = lines.index("nearby tickets:")
nearby_ticket_lines = lines[nearby_start + 1:]

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

rules = [Rule(line) for line in rule_lines]

error_rate = 0

for ticket_line in nearby_ticket_lines:
    ticket_numbers = [int(x) for x in ticket_line.split(",")]
    for number in ticket_numbers:
        if not any(rule.validate(number) for rule in rules):
            error_rate += number

print(error_rate)
