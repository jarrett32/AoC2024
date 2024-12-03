f = open("input.txt", "r")


nums = f.readlines()

def is_valid(r):
    has_error = False
    for i in range(1, len(r)):
        if 1 <= r[i] - r[i - 1] <= 3:
            
            if i == len(r) - 1:
                return True
        else:
            break

    for i in range(1, len(r)):
        if -3 <= r[i] - r[i - 1] <= -1:
            
            if i == len(r) - 1:
                return True
        else:
            break

    return False

def is_valid_brute(r):
    if is_valid(r):
        return True

    for i in range(len(r)):
        new_r = r[:i] + r[i + 1:]
        if is_valid(new_r):
            return True
        
    return False

reports = [x.split(" ") for x in nums]
sol = 0

for r in reports:
    for i in range(len(r)):
        r[i] = int(r[i])

    sol += is_valid_brute(r) 

print(sol)