number = raw_input("Enter a number: ")
new_list = []
for i in range(int(number)):
    if i == 0 or i % 2 == 0:
        new_list.append(i)
print new_list
