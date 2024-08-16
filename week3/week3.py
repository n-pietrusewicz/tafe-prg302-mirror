# fruit_file = open("fruit.txt", 'a')
# count = 0
# fruit_to_add = "x"
# # Starts iteration and asks user for input.
# while fruit_to_add != "":
#     fruit_to_add = input("Add a fruit: ").title()
#     fruit_file.write(f"{fruit_to_add}\n")
#     if fruit_to_add == "":
#         fruit_file.write(f"{fruit_to_add}")
# fruit_file.close()

fruit_file = open("fruit.txt", "r")
for fruit in fruit_file:
    print(fruit.rstrip())
fruit_file.close()

