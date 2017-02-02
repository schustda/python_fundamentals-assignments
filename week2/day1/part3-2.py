number = raw_input("Enter a number: ")
n = raw_input("Enter another number: ")
new_list = []
for i in range(int(number)):
    if i % int(n) == 0:
        new_list.append(i)
print new_list
