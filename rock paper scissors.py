import random

def play():
    user = input("What do you choose?\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice( ['r', 'p', 's'] )
    
    if user == computer:
        return 'Oh! It\'s a tie!'    
        
    # r > s. s > p, p > r
    if is_win(user, computer):
        return 'You won! Congratulations!'
        
    return 'Aw, you lost...'
        
def is_win(player, opponent):
    # return true if player wins
    # r > s. s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return true
        
print(play())