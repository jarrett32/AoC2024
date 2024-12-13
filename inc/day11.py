stones = [0, 7, 198844, 5687836, 58, 2478, 25475, 894]

d = {}

def recursive_iterate(stones, iterations):
    print(f"Iteration {iterations}", len(stones))
    if iterations == 0:
        # Base case: If no more iterations, return the current stones
        return stones

    new_stones = []
    for s in stones:
        if s in d:
            # If the stone has been transformed before, use the cached result
            result = d[s]
            if isinstance(result, list):
                new_stones.extend(result)
            else:
                new_stones.append(result)
            continue

        if s == 0:
            # Rule 1: Stone engraved with 0 becomes 1
            new_stones.append(1)
            d[s] = [1]

        elif len(str(s)) % 2 == 0:
            # Rule 2: Stone with even number of digits is split
            s_str = str(s)
            mid = len(s_str) // 2
            stone1 = int(s_str[:mid])  # Left half
            stone2 = int(s_str[mid:])  # Right half
            new_stones.append(stone1)
            new_stones.append(stone2)
            d[s] = [stone1, stone2]

        else:
            # Rule 3: Multiply the stone's number by 2024
            transformed_stone = s * 2024
            new_stones.append(transformed_stone)
            d[s] = transformed_stone

    # Recur for the next iteration
    return recursive_iterate(new_stones, iterations - 1)


# Perform 75 iterations
final_stones = recursive_iterate(stones, 75)

# Print results
print("Final number of stones:", len(final_stones))
