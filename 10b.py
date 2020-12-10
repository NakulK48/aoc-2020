with open("10.txt") as file_obj:
    lines = [int(line.strip()) for line in file_obj.readlines()]

lines.sort()

# We consider the length of 'runs' of 1-jolt differences
# (bookended by 3-jolt differences)

# A run of 0 here means something like (0) 3 (6)
# 1 would be (0) 3 4 (7)
# 2 would be (0) 3 4 5 (8)
# (remember: a run is always preceded and followed by a 3-jolt difference)

# First, we calculate all the run lengths.

all_runs = []
current_run = 0
prev = 0

for adapter in lines:
    if (adapter - prev) == 3:
        all_runs.append(current_run)
        current_run = 0
    else:
        current_run += 1
    prev = adapter 

# (it's only 4, which is disappointing - that's pretty easy to work out manually)
max_run = max(all_runs)

# The key thing about a 3-jolt difference is that there's only one way to traverse it.
options_by_run_length = {0: 1}

# To get the number of combinations for a given run length, we build up iteratively
# To achieve a run of N, you can achieve a run of N-3, N-2 or N-1 (and then jump 3, 2 or 1)
# e.g. (0) 3 4 5 6 7 8 (11) - to get to the 8 you have to get up to 5, 6 or 7
# So, we just sum all of those together.

for i in range(max_run):
    options_by_run_length[i+1] = sum(options_by_run_length.get(i - j, 0) for j in range(3))

# Every time we have a choice, we can multiply our total number of options
# by the number of options in that choice

result = 1

for run in all_runs:
    result *= options_by_run_length[run]

print(result)
