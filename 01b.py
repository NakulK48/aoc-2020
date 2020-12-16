TARGET = 2020

PAIR_SUMS = {}

def main():
    with open("1.txt") as file_obj:
        lines = file_obj.readlines()
    nums = [int(line.strip()) for line in lines]
    for i, num1 in enumerate(nums):
        for j in range(i+1, len(nums)):
            num2 = nums[j]
            PAIR_SUMS[num1 + num2] = (num1, num2)

    for num in nums:
        partner = TARGET - num
        if partner in PAIR_SUMS:
            partner1, partner2 = PAIR_SUMS[partner]
            return (num * partner1 * partner2)
    return None

print(main())
