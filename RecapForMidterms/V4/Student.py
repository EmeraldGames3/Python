class Student:
    def __init__(self, name: str, university: str):
        self.university = university
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.university}"

    def __repr__(self):
        return f"{self.name}, {self.university}"


student_list = []


def add_student(student: Student):
    student_list.append(student)


def get_student(student_name: str, attr: str):
    for student in student_list:
        if student_name == student.name:
            return student.__getattribute__(attr)


def sort_students():
    student_list.sort(key=lambda x: x.name)


add_student(Student("Mircea", "UBB"))
add_student(Student("Bogdan", "UBB"))
add_student(Student("Radu", "UTCN"))

print(student_list)
sort_students()
print(student_list)

print(get_student("Bogdan", "university"))
