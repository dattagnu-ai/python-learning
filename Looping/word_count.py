names = ["dattu", "shreya", "supriya", "lokesh", "danish", "dinesh"]
count = 0
list = []
for name in names:
    if name.startswith("d"):
        count = count + 1
        list.append(name)
print(count)
print(list)
