# debugging

count = 0
marks_list = []
while count < 5:
    try:
        mark = int(input("Enter a mark (0-100): "))
        if 0 <= mark <=100:
            marks_list.append(mark)
            count += 1
        else:
            print("Oops! Mark must be between 0 and 100.")
    except ValueError:
        print("Oops! Please enter a whole number.")
print("Done.")

print("Summary:")
print(f"Marks entered: {len(marks_list)}\n")

# Sum of marks
print(f"\nSum: {sum(marks_list)}")

# Average of marks
average = sum(marks_list)/len(marks_list)
print(f"Average: {round(average)}")