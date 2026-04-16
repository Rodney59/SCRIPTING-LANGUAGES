class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    def __init__(self, first_name, last_name, group):
        super().__init__(first_name, last_name)
        self.group = group

class Teacher(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department

