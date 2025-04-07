import itertools
from Roster_students import student_roster
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  #task 4
  def student_combination(self):
    combo = list(itertools.combinations(self.sorted_names, 2))
    return combo

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
        if student['favorite_subject'] == subject:
            selected_students.append((student['name'], subject))
    return selected_students
