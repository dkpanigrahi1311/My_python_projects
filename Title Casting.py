
# method-1
def format_name(f_name , l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return (f"{format_f_name} {format_l_name}")

first_name = input()
last_name = input()

print(format_name(first_name, last_name))

# method-2
def format_name(f_name , l_name):
    first_name = f_name[0].upper() + f_name[1:-1].lower() + f_name[-1].lower()
    last_name = l_name[0].upper() + l_name[1:-1].lower() + l_name[-1].lower()
    return f"{first_name} {last_name}"
first_name = input()
last_name = input()

print(format_name(first_name, last_name))