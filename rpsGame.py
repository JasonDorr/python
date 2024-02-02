import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0
gameCount = 0



while gameCount < 5:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('')
    
    while True:
        print('Please choose (r)ock, (p)aper, (s)cissors or (q)uit')
        playerChoice = input() 
        
        print('')
        
        if playerChoice == 'q':
            sys.exit()
            
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break
        else:
            print('Please type r, p, s, or q')

#Display Player's Choice

    if playerChoice == 'r':
        print('Player chooses Rock')
        print('Versus...')
        
    elif playerChoice == 'p':
        print('Player chooses Paper')
        print('Versus...')
        
    elif playerChoice == 's':
        print('Player chooses Scissors')
        print('Versus...')
        
#Display Computer's Choice
    num = random.randint(1, 3)
    
    if num == 1:
        print('Computer chooses Rock')
        computerChoice = 'r'
        
    elif num == 2:
        print('Computer chooses Paper')
        computerChoice = 'p'
        
    elif num == 3:
        print('Computer chooses Scissors')
        computerChoice = 's'
        
#Game Logic
    #Win Conditions
    if playerChoice == computerChoice:
        print("It's a tie!")
        print('')
        ties = ties + 1
        
    if ties == 5:
        break
        
    elif playerChoice == 'r' and computerChoice == 's':
        print('You win! Rock beats Scissors')
        print('')
        wins = wins + 1
        gameCount = gameCount + 1
        
    elif playerChoice == 'p' and computerChoice == 'r':
        print('You win! Paper beats Rock')
        print('')
        wins = wins + 1
        gameCount = gameCount + 1
        
    elif playerChoice == 's' and computerChoice == 'p':
        print('You win! Scissors beats Paper')
        print('')
        wins = wins + 1
        gameCount = gameCount + 1
    
    #Loss Conditions    
    elif computerChoice == 'r' and playerChoice == 's':
        print('You lose! Rock beats Scissors')
        print('')
        losses = losses + 1
        gameCount = gameCount + 1
        
    elif computerChoice == 'p' and playerChoice == 'r':
        print('You lose! Paper beats Rock')
        print('')
        losses = losses + 1
        gameCount = gameCount + 1
        
    elif computerChoice == 's' and playerChoice == 'p':
        print('You lose! Scissors beats Paper')
        print('')
        losses = losses + 1
        gameCount = gameCount + 1
        
if wins > losses:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('You beat the Computer! Great job!')
    
elif wins < losses:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('You lost against the Computer. Get Good.')
    
elif ties == 5:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('How did you you manage that? Try again.')