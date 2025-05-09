import random
word_list = input().split()
word = random.choice(word_list).lower()
life_line = len(word)+ 3
answer = ""
right_count = 0
print("_"*len(word))
display = ("_"*len(word))
for i in range(life_line):
    answer = input("Guess a letter: ").lower()
    if answer in word:
        idx = word.index(answer)
        display = display[:idx] + answer + display[idx+1:]
        print(display)
        right_count += 1
        life_line -= 1
        if right_count == len(word):
            break
    else:
        print(display)

if right_count == len(word):
    print("You Won")
else:
    print("Game Over")




