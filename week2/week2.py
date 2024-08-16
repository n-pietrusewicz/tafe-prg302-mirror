fruit = []  # One = sign is used for assignment
count = 0   # assigning the value of 0 to the variable count
while count < 5:
    fruit_to_add = input("Add a fruit: ").title()
    like = input(f'Do you like to eat {fruit_to_add}? ').lower()
    if like == 'yes' or like == 'y':
        fruit.append(fruit_to_add)
        count = count + 1
    else:
        print(f'OK, I will not save {fruit_to_add} to the list.')
print(f'Your fruits are: {fruit}...')