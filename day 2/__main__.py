inputs = []

horizontal = 0
vertical = 0


with open("inputs.txt", "r") as f:
    f = f.read()
    f = f.splitlines()

    for v in f:
        inputs.append(v)


for value in inputs:

    value = value.split(" ")

    command = value[0]
    num = int(value[1])

    functions = {
        "forward": "+",
        "up": "-",
        "down": "+",
    }

    directions = {"forward": "horizontal", "up": "vertical", "down": "vertical"}

    exec(f"{directions[command]} {functions[command]}= {num}")

