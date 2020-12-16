TARGET = 2020

def main():
    with open("1.txt") as file_obj:
        lines = file_obj.readlines()
    nums = {int(line.strip()) for line in lines}
    for num in nums:
        partner = TARGET - num
        if partner in nums:
            return (num * partner)
    return None

print(main())
