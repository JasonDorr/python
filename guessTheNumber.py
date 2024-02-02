import random

secretNumber = random.randint(1, 20)
print('Try to guess the number between 1 and 20.')
print('You have 6 tries.')

for guesses in range(1, 7):
    guess = int(input())
     
    if guess > secretNumber:
        print('Your guess is too high. Try again.')
        
    
    elif guess < secretNumber:
        print('Your guess is too low. Try again.')
        
    else:
        break
     
if guess == secretNumber:
    print(f'You win! The number was {secretNumber}.')
    print(f'It took you {guesses} tries to get it correct.')
    
else:
    print(f'You lose! The number was {secretNumber}')
    
