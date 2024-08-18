# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

grade = input("Enter grade of student: ")

if not grade.isdigit():
    print("Enter a number, not characters")
else:
    grade = int(grade)
    
    if grade > 100:
        print("You cannot enter marks greater than 100")
    elif grade >= 90:
        print("Your grade is Excellent")
    elif grade >= 80:
        print("Your grade is A")
    elif grade >= 70:
        print("Your Grade is B")
    elif grade >= 60:
        print("Your Grade is C")
    elif grade >= 50:
        print("Your Grade is D")
    else:
        print("You have failed")
