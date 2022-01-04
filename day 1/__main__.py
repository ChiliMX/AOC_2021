all_values = []
total_incs = 0

with open("inputs.txt", "r") as f:
    f = f.read()
    f = f.splitlines()

    for v in f:
        all_values.append(int(v))


for i, value in enumerate(all_values):

    pre_index = all_values[i - 1]
    current_index = all_values[i]

    index_diff = pre_index - current_index

    if i != 0:
        if abs(index_diff) == index_diff:
            print(f"{value} decreased")
        else:
            print(f"{value} increased")
            total_incs += 1
    else:
        print(f"{value} (N/A - no previous measurement)")
