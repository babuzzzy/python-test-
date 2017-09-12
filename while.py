number = 23
running = True

while running:
    guess = int(raw_input('Enter an Integer :'))

    if guess == number:
        print 'Congratulrations, you guessed it.'
        #this causes the while loop to stop
        running = False

    elif guess < number:
        print 'No, it is a little higher than that'

    else:
        print 'The while loop is over'

else:
    print 'No, it is a little lower than that'

print 'done'
