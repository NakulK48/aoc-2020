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

# raw_rules["8"] = "42 | 42 8"
# raw_rules["11"] = "42 31 | 42 11 31"

parsed_rules = {}

# 42 = a
# 31 = b
# ab
# aabb
# aaabbb


def parse(raw):
    if raw == "8":
        regex_42 = parse("42")
        return f"({regex_42})+"
    if raw == "11":
        r42 = parse("42")
        r31 = parse("31")
        choices = [(r42 * x) + (r31 * x) for x in range(1, 10)]
        joined_choices = "|".join(choices)
        return f"({joined_choices})"
    
    if raw in parsed_rules:
        return parsed_rules[raw]

    elif raw == "11":
        pass

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
