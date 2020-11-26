user_input = int(input("Enter the id number: "))
# python class


class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'

    def data(self):
        return "{}\n{}\n{}\n".format(self.first, self.last, self.email)

    def name(self):
        return "{} {}".format(self.first, self.last)


student_ids = range(1, 11)
students = {
    1: Student("Moosa", "Hussain"),
    2: Student("Hamza", "Junaid"),
    3: Student("Ayan", "Faisal"),
    4: Student("Abdul", "Basit")
}

for i in student_ids:
    if i == user_input:
        student = students[user_input]
        print(student.data())


# student1 = Student("Hamza","Junaid")
# print(student1.data())
# print(student1.name())
