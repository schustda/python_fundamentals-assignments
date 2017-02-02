#part 1-1
def divisors(n):
    user_inputted_num = n
    print 'Our divisors are: '
    idx = user_inputted_num
    while idx > 0:
        if user_inputted_num % idx == 0:
            print idx
        idx -= 1

#part 2-2
def least_common_multiple(n,m):
    print 'The least common multiple of these two numbers is: '
    idx = n
    if idx > m:
        idx = m
    while True:
        if  idx % n == 0 and idx % m == 0:
            print idx
            break
        idx += 1
