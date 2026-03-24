#   Accept the marks of 5 subjects, calculate the total and percentage, and display results.

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))

total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:2f}%")