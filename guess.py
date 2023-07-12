
# importing random module
import random

   # Start game level instruction
user_level = input('....Choose Level.... \n\n 1. Beginner(1-20)'
      '\n 2.Intermidiate (1-100) \n 3. Hard (1-1000) \n\n' 
     'Choose Level' )
    
    # Assigning user_level into an integer
user_level = int(user_level)
level=0
if user_level ==1:
   level=20
elif user_level ==2:
   level=100
elif user_level ==3:
   level=1000
else: 
     print('Invalid User Input')
     exit(1)



#Correct  guess number 
chances=0
guess_num = random.randint(1,level)
i=0
while i<5:
   user_input = int( input(f'Guess a number(1-{level}):') )
   chances=chances+1
      
   if user_input==guess_num:
    print('You won, and you used ', chances ,'chances')
    break
   else:
      if user_input>level:
        print('Out Of Range')
      elif user_input > guess_num:
            print("Your Guess is too High....Try Again")   
      else:
         print('Your Guess is too low....Try again')    
  
   i=i+1
     
print('..PROGRAM ENDED, THANKS FOR GUESSING')
 