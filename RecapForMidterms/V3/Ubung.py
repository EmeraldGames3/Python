class Student:
    def __init__(self, id_, name, grade):
        self.grade = grade
        self.name = name
        self.id = id_

    def __str__(self):
        return f"{self.id} {self.name} {self.grade}"

    def __repr__(self):
        return f"{self.id} {self.name} {self.grade}"


def read_from_file():
    with open("text.txt") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def write_to_file(file_content):
    with open("text.txt", "w") as f:
        f.write("\n".join(file_content))


def add_student_to_file(file_content: list[str], student: Student):
    file_content.append(str(student))
    write_to_file(file_content)


def best_student():
    # Extract the contents of the file and convert them to a list of students
    file_content = read_from_file()
    file_content = list(map(lambda x: x.split(), file_content))
    file_content = list(map(lambda x: Student(int(x[0]), x[1], int(x[2])), file_content))

    # Sort the list of students after their grades
    file_content.sort(key=lambda x: x.grade, reverse=True)

    # print(file_content)

    return file_content[0]


print(best_student())

# add_student_to_file(read_from_file(), Student(1, "Mircea", 3))


def modify_student_name(file_content: list[str], student: Student, new_name: str):
    student_str = str(student)

    if student_str not in file_content:
        return

    file_content[file_content.index(str(student_str))] = str(
        Student(id_=student.id, name=new_name, grade=student.grade))
    write_to_file(file_content)

# modify_student_name(read_from_file(), Student(1, "Mircea", 3), "Miclaus")
