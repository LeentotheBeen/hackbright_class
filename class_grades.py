#turn into a list


with open("class_grades.txt") as class_grades:
    class_grades = class_grades.readlines()

for grade in class_grades:
    grade = int(grade)
    if grade > 90:
        print "%s is an A" %(grade)
    elif grade >= 80:
        print "%s is a B" %(grade)
    elif grade >= 70:
         print "%s is a C" %(grade)
    elif grade >= 60:
         print "%s is a D" %(grade)
    else:
        print "%s is a F" %(grade)
