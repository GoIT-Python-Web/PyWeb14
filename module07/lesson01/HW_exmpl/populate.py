from models import Student, Group, Subject, Tutor, Grade, session
from random import randint

group =  Group(name="main group")
student1 = Student(fullname="John Dou", group=group)
student2 = Student(fullname="John Gou", group=group)
student3 = Student(fullname="John Bou", group=group)
student4 = Student(fullname="John Jou", group=group)

tutor = Tutor(fullname='John Show')
python = Subject(name='Python',tutors=[tutor])

session.add(group)
session.add(tutor)
session.add(student1)
session.add(student2)
session.add(student3)
session.add(student4)
session.commit()


for student in group.students:
    grade = Grade(grade=randint(1,12), student=student, subject=python)
    session.add(grade)

session.commit()


g = session.query(Grade).all()
for i in g:
    print('****************')
    print(i.student.fullname)
    print(i.subject.name)
    print(i.grade)
    print(i.subject.tutors[0].fullname)




