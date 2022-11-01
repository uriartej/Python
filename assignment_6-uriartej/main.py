from people import Faculty
from people import Student

def printMenu():
    print('\n      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU ***')
    print('1. Add faculty')
    print('2. Print faculty')
    print('3. Add student')
    print('4. Print student')
    print('9. Exit the program\n')
    c = input('Enter menu choice: ')
    return c

        # populating list to test print functions easier, add functions still work
james = Faculty('James', 'Corden', 'Clown')
faculty_list = [james]

        # populating list to test print functions easier, add functions still work
scott = Student('Scott', 'Dolphin')
scott.set_class('sophomore')
scott.set_major('cs')
scott.set_advisor(faculty_list[0])
student_list = [scott]

while True:
    answer = printMenu()
    
    match answer:
        case '1':
            fname = input('Enter first name: ')
            lname = input('Enter last name: ')
            dept = input('Enter Department: ')
            f = Faculty(fname, lname, dept)
            faculty_list.append(f)
        case '2':
            print('\n======================= FACLUTY =======================')
            print('Record  Name                  Department')
            print('======  ====================  =========================')
            record = 0
            for fac in faculty_list:
                print(f'{str(record):8}{fac.getName():22}{fac.department:25}')
                record += 1

        case '3':
            fname = input('Enter first name: ')
            lname = input('Enter last name: ')
            s = Student(fname, lname)
            s.set_class(input('Enter Class year: '))
            s.set_major(input('Enter Major: '))
            r = int(input('Enter Advisor record number: '))
            s.set_advisor(faculty_list[r])
            student_list.append(s)

                            
        case '4':
            print('\n===================================== STUDENTS ======================================')
            print('Name                  Class      Major                      Advisor')
            print('====================  ========   =========================  =========================')
            record = 0
            for stu in student_list:
                print(f'{stu.getName():22}{str(stu.classyear):11}{stu.major:27}{stu.advisor.getName():25}')
        case '9':
            break