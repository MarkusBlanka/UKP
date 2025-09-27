import random


guess = random.randint(1, 1000)
higher_bound = 1000
lower_bound = 1
while True:
    print(guess)
    response = input()

    if "low" in response:
        lower_bound = guess + 1
        guess = random.randint(lower_bound, higher_bound)
        
    elif "high" in response:
        higher_bound = guess - 1
        guess = random.randint(lower_bound, higher_bound)
        
    else:
        exit()