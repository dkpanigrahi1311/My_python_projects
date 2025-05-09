def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    love_score = str(true_count) + str(love_count)
    print(love_score)

name1 = input("Enter your name: ")
name2 = input("Enter your BF's/GF's name: ")
calculate_love_score(name1,name2)