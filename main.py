# Домашняя Работа задача 3
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


lecturer1 = Lecturer("Ivan", "Petrov")
lecturer1.courses_attached.append("Python")
lecturer2 = Lecturer("Anna", "Sidorova")
lecturer2.courses_attached.append("Python")

reviewer = Reviewer("Some", "Buddy")
reviewer.courses_attached.append("Python")

student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress.extend(["Python", "Git"])
student1.finished_courses.append("Введение в программирование")

student2 = Student("Alice", "Smith", "female")
student2.courses_in_progress.append("Python")


reviewer.rate_hw(student1, "Python", 9)
reviewer.rate_hw(student1, "Python", 10)
reviewer.rate_hw(student2, "Python", 8)


student1.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "Python", 8)


print("--- Reviewer ---")
print(reviewer)

print("\n--- Lecturer 1 ---")
print(lecturer1)

print("\n--- Lecturer 2 ---")
print(lecturer2)

print("\n--- Student 1 ---")
print(student1)

print("\n--- Student 2 ---")
print(student2)

print("\nСравнение лекторов:")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

print("\nСравнение студентов:")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")