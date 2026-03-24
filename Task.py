#write a program to accept marks obtained in 5 subjects and store into list
#display total marks
#calculate percentage
#display grades using following conditions
# % 75 or above : distinction
# % 60 or above : first class
# % 50 or above : second class
# % 40 or above : pass 
# % below 40 : fail
#print maximum marks
#print minimum marks


name= input("Enter student name: ")
marks = []
for i in range(5):
    mark = int(input("Enter marks for subject: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100

print("Total Marks: ", total_marks)
print("Percentage: ",percentage)
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Pass")
else:
    print(name," is Fail")


print("Maximum Marks: ", max(marks))
print("Minimum Marks: ", min(marks))