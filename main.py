# Домашняя Работа задача № 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс для лекторов (наследуется от Mentor)."""
    pass


class Reviewer(Mentor):
    """Класс для проверяющих (наследуется от Mentor)."""

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"



best_student = Student("Ruoy", "Eman", "male")
best_student.courses_in_progress.append("Python")

cool_reviewer = Reviewer("Some", "Buddy")
cool_reviewer.courses_attached.append("Python")

cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 9)
cool_reviewer.rate_hw(best_student, "Python", 8)

print(best_student.grades)