class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade = 0

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                sum_grades = 0
                count_grades = 0
                keys = lecturer.grades.keys()
                for key in keys:
                    sum_grades += sum(lecturer.grades[key])
                    count_grades += len(lecturer.grades[key])
                if count_grades == 0:
                    lecturer.av_grade = 0
                else:
                    lecturer.av_grade = sum_grades/count_grades
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗакончил курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Второй не является студентом")
            return
        return self.av_grade < other.av_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
        self.av_grade = 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Второй не является лектором")
            return
        return self.av_grade < other.av_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                sum_grades = 0
                count_grades = 0
                keys = student.grades.keys()
                for key in keys:
                    sum_grades += sum(student.grades[key])
                    count_grades += len(student.grades[key])
                if count_grades == 0:
                    student.av_grade = 0
                else:
                    student.av_grade = sum_grades/count_grades
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


best_student = Student('Иван', 'Иванов', 'муж')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['SQL']

cool_lecturer = Lecturer('lecturer 1', 'lecturer 11')
cool_lecturer.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)

cool_reviewer = Reviewer('Some2', 'Body2')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

best_student2 = Student('Пётр', 'Петров', 'муж')
best_student2.courses_in_progress += ['Английский для программистов']
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['GIT']

cool_lecturer2 = Lecturer('lecturer 2', 'lecturer 22')
cool_lecturer2.courses_attached += ['GIT']
best_student2.rate_hw(cool_lecturer2, 'Python', 10)
best_student2.rate_hw(cool_lecturer2, 'Python', 7)

cool_reviewer2 = Reviewer('Some2', 'Body2')
cool_reviewer2 = Reviewer('Some2', 'Body2')
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['Java']
cool_reviewer2.rate_hw(best_student2, 'Python', 5)
cool_reviewer2.rate_hw(best_student2, 'Python', 8)
cool_reviewer2.rate_hw(best_student2, 'Python', 6)
cool_reviewer2.rate_hw(best_student2, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'Python', 6)
cool_reviewer2.rate_hw(best_student2, 'Java', 10)
cool_reviewer2.rate_hw(best_student2, 'Java', 9)
cool_reviewer2.rate_hw(best_student2, 'Java', 10)



print(best_student2)
print(cool_lecturer2)
print(cool_reviewer2)


print(best_student>best_student2)
print(cool_lecturer<cool_lecturer2)

print("___________________________________")

students = [best_student, best_student2]
lecturers = [cool_lecturer, cool_lecturer2]
course = 'Python'


def aver_all_students(students,course):
    sum_grades = 0
    count_grades = 0
    average_grades = 0
    for student in students:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    if count_grades == 0:
        average_grades = 0
    else:
        average_grades = sum_grades / count_grades
    return average_grades

def aver_all_lecturers(lecturers,course):
    sum_grades = 0
    count_grades = 0
    average_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
    if count_grades == 0:
        average_grades = 0
    else:
        average_grades = sum_grades / count_grades
    return average_grades
    
print(aver_all_lecturers(lecturers,course))
print(aver_all_students(students,course))