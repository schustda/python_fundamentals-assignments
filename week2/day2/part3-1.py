x = [int(i) for i in raw_input("Enter numbers separated by commas: ").split(',')]
y = [int(i) for i in raw_input("Enter more numbers separated by commas: ").split(',')]
print set(x).intersection(set(y))
