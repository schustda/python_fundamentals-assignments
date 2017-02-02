x = int(raw_input("Input a number "))
factorial = 1
prime = ''
for i in range(x):
    factorial *= (i + 1)    #add one because the first index is 0
for i in range(x-3):
    if x % (i + 2) == 0:
        prime = ' not'
print "The factorial of " + str(x) + " is " + str(factorial) + ', and it is' + prime + ' a prime number'
