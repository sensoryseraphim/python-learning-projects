import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess =  random.randint(low, high)
        else:
            guess = low #could also be high who cares
        feedback =  input(f'is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high - guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'The number was {guess}! I got it right!')
    
guess(100)