n_of_bits = int(input())
print(f"{1} {n_of_bits}")

i = 0
while i < 125:
    bit_array = [int(x) for x in input().split()]
    percentage = int(input())
    if percentage >= 70:
        break
    # find longest range of consecurtive 0s
    longest_range = 0
    current_range = 0
    indices_longest_range = []
    for j, bit in enumerate(bit_array):
        if bit == 0:
            current_range += 1
            longest_range = max(longest_range, current_range)
            if current_range == longest_range:
                indices_longest_range = [j - current_range + 1, j]
        else:
            current_range = 0
    print(f"{indices_longest_range[0] + 1} {indices_longest_range[1] + 1}")
    i += 1