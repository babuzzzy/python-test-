def print_max(x,y):
    ''' Prints the maximum of two numbers

    the two values must be integers. '''
    # convert to integers, if possible
    x=int(x)
    y=int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(3,5)
print print_max.__doc__

print 'test'

help(print_max)
