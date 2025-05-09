class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades:
            total = sum([sum(grades) for grades in self.grades.values()])
            count = sum([len(grades) for grades in self.grades.values()])
            return total / count
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"\tИмя: {self.name}\n"
                f"\tФамилия: {self.surname}\n"
                f"\tСредняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"\tКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"\tЗавершенные курсы: {', '.join(self.finished_courses)}\n")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            total = sum([sum(grades) for grades in self.grades.values()])
            count = sum([len(grades) for grades in self.grades.values()])
            return total / count
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"\tИмя: {self.name}\n"
                f"\tФамилия: {self.surname}\n"
                f"\tСредняя оценка за лекции: {avg_grade:.1f}\n")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"\tИмя: {self.name}\n\tФамилия: {self.surname}\n"


# Функции для подсчета средних оценок
def average_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0


def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0


# Создание экземпляров
student1 = Student('Nikita', 'Radchenko', 'male')
student1.courses_in_progress += ['Python', 'OOP']
student1.finished_courses += ['Git']

student2 = Student('Olga', 'Eremina', 'female')
student2.courses_in_progress += ['Python', 'OOP']
student2.finished_courses += ['Git']

lecturer1 = Lecturer('Pavel', 'Molibog')
lecturer1.courses_attached += ['OOP']

lecturer2 = Lecturer('Timur', 'Anvartdinov')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Oleg', 'Bulygin')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Elena', 'Nikitina')
reviewer2.courses_attached += ['OOP']

# Оценки лектора студентом
student1.rate_lecturer(lecturer1, 'OOP', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)

student2.rate_lecturer(lecturer1, 'OOP', 10)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Оценки студента проверяющим
reviewer1.rate_hw(student1, 'Python', 9,)
reviewer1.rate_hw(student2, 'Python', 8,)

# Вывод информации о студентах, лекторах и проверяющих
print('Студенты:')
print(student1)
print(student2)
print('Лекторы:')
print(lecturer1)
print(lecturer2)
print('Проверяющие:')
print(reviewer1)
print(reviewer2)

# Средние оценки
print(f"Средняя оценка студентов по курсу Python: {average_student_grade([student1, student2], 'Python'):.1f}")
print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade([lecturer1, lecturer2], 'Python'):.1f}\n")

# Лучшие студенты и лекторы
if student1.average_grade() >= student2.average_grade():
    print(f'Лучший студент - {student1.name} {student1.surname}')
else:
    print(f'Лучший студент - {student2.name} {student2.surname}')

if lecturer1.average_grade() >= lecturer2.average_grade():
    print(f'Лучший лектор - {lecturer1.name} {lecturer1.surname}')
else:
    print(f'Лучший лектор - {lecturer2.name} {lecturer2.surname}')