with open("input.txt", "r") as f:
    text = f.readlines()

totals = [int(line.split(":")[0].strip()) for line in text]
equations = [list(map(int, line.split(":")[1].strip().split())) for line in text]

sol = 0

def eval_equation(running_sum, equation, total):

    
    if running_sum > total:
        return False
    
    if not equation:
        return running_sum == total
    
    current = equation[0]
    rest = equation[1:]

    return (eval_equation(running_sum + current, rest, total) or
            eval_equation(running_sum * current, rest, total))



for i in range(len(totals)):

    if eval_equation(0, equations[i], totals[i]):
        sol += int(totals[i])




print(sol)