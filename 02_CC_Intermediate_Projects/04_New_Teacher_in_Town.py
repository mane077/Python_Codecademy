import itertools
from Roster_students import student_roster
from classroom_organizer import ClassroomOrganizer

student_iterator = iter(student_roster)
#task2
#for i in range(10):
#  print(next(student_iterator))
#for student in student_iterator:
#  print(student)

#task4
y = ClassroomOrganizer()
print(y.student_combination())

#task 5
Student_Math_Science = y.get_students_with_subject("Math") + y.get_students_with_subject("Science")
print(Student_Math_Science)
print("Total students with Math and Science: " + str(len(Student_Math_Science)))

print(list(itertools.combinations(Student_Math_Science, 4)))
print("Combinations possible math+science, 4 at a table: " + str(len(list(itertools.combinations(Student_Math_Science, 4)))))



