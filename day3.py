import re


f = open("input.txt", "r")
text = f.read()

# reg = r"mul\(\d+,\d+\)"
reg = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

matches = re.findall(reg, text)

sum = 0
do = True
for m in matches:

    if m == "do()":
        do = True
        continue
    if m == "don't()":
        do = False
        continue

    if m[:4] == "mul(" and do:
        s = m[4:-1].split(",")
        sum += int(s[0]) * int(s[1])
        continue


print(sum)