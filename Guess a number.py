import random
list_random_numbers = list(range(1,101))

def guess_number(attempts):
    global list_random_numbers
    random_number = int(random.choice(list_random_numbers))
    count = 0
    for i in range(1,attempts+1):
        number = int(input("Enter a number: - "))
        if number == random_number:
            print(f"You got a number and the number is {random_number}")
            count += 1 
            break
        elif number > random_number:
            print("Too High")
            print(f"You have {attempts-i} attempts to guess a number")
        elif number < random_number:
            print("Too Low")
            print(f"You have {attempts-i} attempts to guess a number")
    if count == 1:
        pass
    else:
        print(f"Actuall Random number is {random_number} ")

def choose_difficulty(difficulty):
    if difficulty == "easy":
        print("Number of attemts are 10")
        attempts = 10
        guess_number(attempts)
    elif difficulty == "hard":
        print("Number of attemts are 5")
        attempts = 5 
        guess_number(attempts)
    else:
        print("Type 'easy' or 'hard' only")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': - ")
        return choose_difficulty(difficulty)
    
print("Welcome to the number guessing game")
print("I think a number is between 1 to 200")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': - ")
choose_difficulty(difficulty)