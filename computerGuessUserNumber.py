import random

def computerGuess(x):

    low = 1
    high = x
    feedback = ""
    tries = 0

    while feedback != "=":
        guess = random.randint(low, high)
        feedback = input(f"{guess} is too high(h), too low(l) or correct(=)? ")

        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
        tries += 1
        
    if tries == 1:
        print(f"""
    The number is {guess}.
    It only took me {tries} try.""")
    else:
        print(f"""
    The number is {guess}.
    It only took me {tries} tries.""")
    

Range = int(input("Maximum number: "))
computerGuess(Range)
