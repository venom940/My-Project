# Importing random module
import random

# Correct guess number
guess_num = random.randint 
i=0
while i<5:
 user_input = int( input('Guess a number') )
 if user_input==guess_num:
    print('Correct')
 else:
    print('Try Again')
i=i+1   


