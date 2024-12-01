f = open("input.txt", "r")


nums = f.readlines()

left_nums = [int(x.split()[0]) for x in nums]
right_nums = [int(x.split()[1]) for x in nums]

left_nums.sort()
right_nums.sort()

total_diff = 0
for i in range(len(left_nums)):
    total_diff += abs(left_nums[i] - right_nums[i])

print(total_diff)

sim_sol = 0
# part 2
for l in left_nums:
    sim_sol += (l * right_nums.count(l))

print(sim_sol)