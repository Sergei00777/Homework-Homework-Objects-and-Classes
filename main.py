# Домашняя Работа задача 4
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

    def __str__(self):
        avg_grade = self._get_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def _get_avg_grade(self):
        """Вспомогательный метод для вычисления средней оценки."""
        if not self.grades:
            return 0.0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self._get_avg_grade() < other._get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self._get_avg_grade() > other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self._get_avg_grade() == other._get_avg_grade()

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

    def __str__(self):
        avg_grade = self._get_avg_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg_grade:.1f}"
        )

    def _get_avg_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self._get_avg_grade() < other._get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self._get_avg_grade() > other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self._get_avg_grade() == other._get_avg_grade()

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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def calculate_avg_hw_grade(students, course):
    """Средняя оценка за ДЗ по всем студентам в рамках курса."""
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0.0

def calculate_avg_lecture_grade(lecturers, course):
    """Средняя оценка за лекции всех лекторов в рамках курса."""
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0.0

lecturer1 = Lecturer("Ivan", "Petrov")
lecturer1.courses_attached.append("Python")
lecturer2 = Lecturer("Anna", "Sidorova")
lecturer2.courses_attached.append("Python")

reviewer1 = Reviewer("Oleg", "Kuznet")
reviewer1.courses_attached.append("Python")

reviewer2 = Reviewer("Elena", "Smirnova")
reviewer2.courses_attached.append("Git")

student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress.extend(["Python", "Git"])
student1.finished_courses.append("Введение в программирование")

student2 = Student("Alice", "Smith", "female")
student2.courses_in_progress.append("Python")

reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student2, "Python", 8)

reviewer2.rate_hw(student1, "Git", 7)

student1.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "Python", 8)

print("--- Проверяющие ---")
print(reviewer1)
print("\n" + str(reviewer2))

print("\n--- Лекторы ---")
print(lecturer1)
print("\n" + str(lecturer2))

print("\n--- Студенты ---")
print(student1)
print("\n" + str(student2))

print("\nСравнение лекторов:")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")

print("\nСравнение студентов:")
print(f"student1 > student2: {student1 > student2}")

avg_hw = calculate_avg_hw_grade([student1, student2], "Python")
avg_lecture = calculate_avg_lecture_grade([lecturer1, lecturer2], "Python")

print("\n--- Средние оценки по курсу Python ---")
print(f"Средняя оценка за ДЗ: {avg_hw:.1f}")
print(f"Средняя оценка за лекции: {avg_lecture:.1f}")