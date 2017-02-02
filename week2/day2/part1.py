lst = [int(x) for x in raw_input("Enter a number set separated by commas: ").split(',')]
if len(lst) % 2 == 0:
    del lst[-1]
x = lst[0::2]
y = lst[1::2]
z = zip(x,y)
print z
