# Домашняя Работа задача 2
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Метод для оценки лекторов студентами."""
        if (
                isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс для лекторов (наследуется от Mentor)."""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    """Класс для проверяющих (наследуется от Mentor)."""

    def rate_hw(self, student, course, grade):
        """Метод для оценки домашних работ студентов."""
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


cool_lecturer = Lecturer("Ivan", "Petrov")
cool_lecturer.courses_attached.append("Python")

cool_reviewer = Reviewer("Anna", "Sidorova")
cool_reviewer.courses_attached.append("Python")

best_student = Student("Ruoy", "Eman", "male")
best_student.courses_in_progress.append("Python")

cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 9)
cool_reviewer.rate_hw(best_student, "Python", 8)

best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 9)

print("Оценки студента:", best_student.grades)
print("Оценки лектора:", cool_lecturer.grades)