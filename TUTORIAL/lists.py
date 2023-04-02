demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numbers_list = list((1, 2, 3, 4))
print(type(numbers_list))

r = list(range(1, 100))
print(r)

print(len(demo_list))

print(colors[-2])

print(dir(colors))

colors.append("violet")

colors.extend(["violet", "yellow"])

colors.extend(["pink", "black"])

print(colors)