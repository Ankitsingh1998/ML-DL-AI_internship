import random
chosen_number = random.randint(1,10)
my_number = int(input('Enter a number in between 1 and 10: '))

if my_number == chosen_number:
    print('You win and computer loses.')
else:
    print('Computer wins and you lose.')
    
    
