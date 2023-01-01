students_score = int(input("enter the score in number. "))

if students_score >= 90:
    print("The student's score is %s and grade is 'A'" %(students_score))
elif students_score >=80:
    print("The student's score is %s and grade is 'B'" % (students_score))
elif students_score >=70:
    print("The student's score is %s and grade is 'C'" % (students_score))
elif students_score >=60:
    print("The student's score is %s and grade is 'D'" % (students_score))
else:
    print("The student's score is %s and grade is 'F'" % (students_score))

#method-2

students_score = int(input("enter the score in number. "))

if students_score >= 90:
    print("The student's score is %s and grade is 'A'" %(students_score))
else:
    if students_score >= 80:
        print("The student's score is %s and grade is 'B'" % (students_score))
    else:
        if students_score >= 70:
            print("The student's score is %s and grade is 'C'" % (students_score))
        else:
            if students_score >= 60:
                print("The student's score is %s and grade is 'D'" % (students_score))

            else:
                print("The student's score is %s and grade is 'F'" % (students_score))
