#part 1-1
def factorial(x):
    factorial = 1
    for i in range(1,x+1):
        factorial *= i
    print "The factorial of " + str(x) + " is " + str(factorial)

#part 1-2
def prime(x):
    prime = ''
    for i in range(x-3):
        if x % (i + 2) == 0:
            prime = ' not'
    print '%s is%s a prime number' % (str(x),prime)
