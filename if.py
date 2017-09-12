number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # new block starts here
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'

elif guess < number:
    # Aonother block
    print 'No. it is a little higher than that'
    #You can do whatever you want in a block
else:
    print 'No, it is a little lover than that'


print 'Done'
# this last statement is always executed
# after the if statement is executed

