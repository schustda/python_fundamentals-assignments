m = [int(x) for x in raw_input("Enter numbers separated by dashes: ").split("-")]
n = [x**2 for x in m]
print dict(zip(m,n))
