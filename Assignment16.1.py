def write_student_names(filename="student.txt", names=None):
    if names is None:
        names = ["Alisha", "Bobby", "Charlie", "Diksha", "Eve"]
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + "\n")

write_student_names()