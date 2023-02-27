from main import User
from main import Student

myusers = User.select()
for user in myusers:
    print(user.name, user.email, user.password)

mystudents = Student.select()
for student in mystudents:
    print(student.student_name, student.student_id, student.student_class)