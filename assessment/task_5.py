# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 5

count = 0

marks_list = []
while count < 5:
    try:                                            # While the variable 'count' is less than '5', then try the following procedure:
        mark = int(input("Enter a mark: ")) # Ask the user for their input, store it in the variable 'mark' as an integer.
        if 0 <= mark <= 100:                        # If 0 is <=  mark AND <= 100 do:
            marks_list.append(mark)                 
            count += 1
        else:
            print("Oops! Mark must be between 0 and 100.")
    except ValueError:                              # If there is a ValueError (i.e. a string, negative int or float...)
        print("Oops! Please enter a whole number.")
print("Done.")

print("Summary:\n")
print(f"Marks entered: {len(marks_list)}\n")       # Take the length of the list marks_list and print it.

# Sum of marks
print(f"Sum: {sum(marks_list)}")                 # Add the contents of the list.

# Average of marks
average = sum(marks_list) / len(marks_list)
print(f"Average: {average:.2f}")                   # Prints the average and formats to two decimal places.