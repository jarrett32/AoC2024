f = open("input.txt", "r")
text = f.readlines()

d = {}
page_orders = []
for i, line in enumerate(text):
    if i > 1176:
        page_orders.append(line.strip())
        continue
    line = line.strip()
    if line == "":
        continue
    key, value = line.split("|")
    if key not in d:
        d[int(key)] = set()
    d[int(key)].add(int(value))

sol = 0
page_orders = [[int(num) for num in l.split(",")] for l in page_orders]

def is_correct_order(order, d):
    # {18: 0, 46: 1, 96: 2 ...}
    position = {page: i for i, page in enumerate(order)}
    for x, after_set in d.items():
        if x in position:
            for y in after_set:
                if y in position:
                    if position[x] >= position[y]:
                        return False

    return True


total = 0
for order in page_orders:
    if is_correct_order(order, d):
        middle_index = len(order) // 2
        total += order[middle_index]
    break

print(total)
