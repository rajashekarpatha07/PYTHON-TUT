mark1 = int(input("Enter marks1: "))
mark2 = int(input("Enter marks2: "))
mark3 = int(input("Enter marks3: "))

total_persentage = 100*(mark1+mark2+mark3)/300

if(total_persentage>=40 and mark1>=33 and mark2>=33 and mark3 >= 33):
    print(f"You passed in {total_persentage}")
else:
    print(f"you failed Better luck next time you got {total_persentage}%")