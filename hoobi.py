# class Figure:
#     unit = 'cm'
#
#     def __init__(self):
#         self.__calculate_perimeter()
#         self.calculate_area()
#
#     def get_perimeter(self):
#         return self.__perimeter
#
#     def set_perimeter(self, perimeter):
#         self.__perimeter = perimeter
#
#     def calculate_area(self):
#         pass
#
#     def __calculate_perimeter(self):
#         pass
#
#     def info(self):
#         pass
#
#
# class Square(Figure):
#     def __init__(self, __side_length):
#         self.__side_length = __side_length
#         self.calculate_area()
#         self.perimeter = self.__calculate_perimeter()
#
#     def calculate_area(self):
#         return self.__side_length * 2
#
#     def __calculate_perimeter(self):
#         return self.__side_length * 4
#
#     def info(self):
#         print(
#             f"Square:   Side length:{self.__side_length}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")
#
#
# class Rectangle(Figure):
#
#     def __init__(self, __length, __width):
#         self.__width = __width
#         self.__length = __length
#
#     def calculate_area(self):
#         return self.__length * self.__width
#
#     def __calculate_perimeter(self):
#         return (self.__length + self.__width) * 2
#
#     def info(self):
#         print(
#             f"Rectangle: Length:{self.__length}{self.unit}   Width:{self.__width}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")
#
#
# sq1 = Square(2)
# sq2 = Square(4)
#
# rec1 = Rectangle(5, 8)
# rec2 = Rectangle(1, 3)
# rec3 = Rectangle(1, 4)
#
# general = [sq1, sq2, rec1, rec2, rec3]
# for i in general:
#     i.info()


class Person:
    def __init__(self, fullname: str, age: int, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname: {self.fullname}\n"
              f"Age: {self.age}\n"
              f"is_married: {self.is_married}\n")

    def output(self):
        return f"fullname: {self.fullname}\n" \
               f"Age: {self.age}\n" \
               f"Is married: {self.is_married}\n"


class Student(Person):
    marks = {"English": 0,
             "Russian": 0,
             "Story": 0,
             "Math": 0}

    def __init__(self, marks, fullname, age, is_married):
        super().__init__(fullname, age, is_married)
        self.marks = marks


class Teacher(Person):
    salary = 30000

    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.experience = experience

    def The_salary(self, experience, salary):
        global procent_experience
        self.experience = experience
        self.salary = salary

    def Teacher_salary(self):
        if self.experience >= 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary

    def results(self, experience, salary):
        Person.introduce_myself()
        self.experience = experience
        self.salary = salary
        teacher_esen = Teacher('name: Мээрим')
        print(teacher_esen)


def create_student(st1, st2, st3):
    st1 = Student(fullname="Мээрим", age=20, is_married=False)
    st2 = Student(fullname="Арген", age=20, is_married=False)
    st3 = Student(fullname="Адилет", age=22, is_married=True)

    create_students = [st1, st2, st3]
    return create_students

    students = create_students()
    for i in students:
        studentsss = []
        for marks in i.marks.values:
            studentsss.append(marks)
        print(f"Имя: {i.fullname}\n"
              f"Возраст: {i.age}\n"
              f"Женат?: {i.is_married}"
              f"Средние баллы: {sum(studentsss) / len(studentsss)}\n")
