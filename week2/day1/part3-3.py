a = [0, 3, 6, 9, 10, 2, 5]
b = [2, 6, 4, 7, 8, 1, 15]
new_list = []
for i in a:
    for z in b:
        if i == z:
            new_list.append(i)
print sorted(new_list)
