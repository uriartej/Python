class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name


class Faculty(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name,)
        self.department = department


    def getName(self):
        return self.firstname + ' ' + self.lastname

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def set_class(self, class_year):
        self.classyear = class_year

    def set_major(self, major):
        self.major = major

    def set_advisor(self, advisor):
        self.advisor = advisor

    def getName(self):
        return self.firstname + ' ' + self.lastname
