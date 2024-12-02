f = open("input.txt", "r")


nums = f.readlines()

reports = [x.split(" ") for x in nums]
sol = 0

for r in reports:
    for i in range(len(r)):
        r[i] = int(r[i])

for r in reports:

    diff_one = r[1] - r[0]
    if 1 <= diff_one <= 3:
        inc = True
    elif -3 <= diff_one <= -1:
        inc = False
    else:
        continue

    i = 2
    has_bad = False
    while i < len(r):
        diff = r[i] - r[i - 1]

        if inc and 1 <= diff <= 3:
            i += 1
        elif not inc and -3 <= diff <= -1:
            i += 1
        else:
            if not has_bad:
                has_bad = True
                
                # we can either remove the r or remove r + 1
                if i + 1 < len(r) and (
                    1 <= r[i + 1] - r[i - 1] <= 3 if inc else -3 <= r[i + 1] - r[i - 1] <= -1
                ):
                    r[i] = r[i - 1]
                elif i + 1 < len(r):
                    r[i + 1] = r[i]
                else:
                    break 
            else:
                break

        if i == len(r) - 1:
            sol += 1
            break


print(sol)