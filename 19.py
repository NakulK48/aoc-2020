import re

with open("19.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

blank_index = lines.index("")
rule_lines = lines[:blank_index]
value_lines = lines[blank_index+1:]

raw_rules = {}

for line in rule_lines:
    rule_id, raw_rule = line.split(": ")
    raw_rules[rule_id] = raw_rule

parsed_rules = {}

def parse(raw):
    if raw in parsed_rules:
        return parsed_rules[raw]

    if raw.startswith('"'):
        return raw.replace('"', '')

    or_branches = raw.split(" | ")
    if len(or_branches) == 2:
        left, right = or_branches
        return f"({parse(left)}|{parse(right)})"
    and_branches = raw.split(" ")
    if len(and_branches) == 2:
        left, right = and_branches
        return f"{parse(left)}{parse(right)}"

    # Must be a single ID
    parsed = parse(raw_rules[raw])
    parsed_rules[raw] = parsed
    return parsed

regex = re.compile(parse("0"))

result = sum(1 for value in value_lines if regex.fullmatch(value))
print(result)
