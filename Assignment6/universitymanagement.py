class Person:
    def __init__(self, name, age, contact_info):
        self.name = name
        self._age = age      
        self._contact_info = contact_info   
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")
    
    def get_contact_info(self):
        return self._contact_info
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self._age}, Contact: {self._contact_info}")


class Student(Person):
    def __init__(self, name, age, contact_info, student_id, department):
        super().__init__(name, age, contact_info)
        self.student_id = student_id
        self.department = department
        self.courses = []
        self.grades = {}
    
    def enroll_course(self, course):
        self.courses.append(course)
    
    def get_grades(self):
        return self.grades
    
    def calculate_gpa(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Department: {self.department}")
    
    def display_details(self):
        super().display_details()
        print(f"Student ID: {self.student_id}, Department: {self.department}, Courses Enrolled: {[course.course_name for course in self.courses]}")

class Faculty(Person):
    def __init__(self, name, age, contact_info, faculty_id, department, salary):
        super().__init__(name, age, contact_info)
        self.faculty_id = faculty_id
        self.department = department
        self.courses_assigned = []
        self.salary = salary
    
    def assign_course(self, course):
        self.courses_assigned.append(course)
    
    def get_salary(self):
        return self.salary
    
    def display_info(self):
        super().display_info()
        print(f"Faculty ID: {self.faculty_id}, Department: {self.department}, Salary: {self.salary}")
    
    def display_details(self):
        super().display_details()
        print(f"Faculty ID: {self.faculty_id}, Department: {self.department}, Salary: {self.salary}, Courses Assigned: {[course.course_name for course in self.courses_assigned]}")


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.faculty = None
        self.students_enrolled = []
    
    def add_student(self, student):
        self.students_enrolled.append(student)
    
    def assign_faculty(self, faculty):
        self.faculty = faculty
    
    def display_details(self):
        print(f"Course ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credits}, Faculty: {self.faculty.name if self.faculty else 'Not Assigned'}, Students Enrolled: {[student.name for student in self.students_enrolled]}")


class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.faculty_list = []
        self.student_list = []
        self.courses_offered = []
    
    def add_faculty(self, faculty):
        self.faculty_list.append(faculty)
    
    def add_student(self, student):
        self.student_list.append(student)
    
    def list_courses(self):
        for course in self.courses_offered:
            print(f"Course: {course.course_name}, Credits: {course.credits}")
    
    def display_details(self):
        print(f"Department ID: {self.department_id}, Name: {self.name}")
        print(f"Faculty Members: {[faculty.name for faculty in self.faculty_list]}")
        print(f"Students Enrolled: {[student.name for student in self.student_list]}")
        print(f"Courses Offered: {[course.course_name for course in self.courses_offered]}")


class University:
    _instance = None
    
    def __new__(cls, university_name):
        if not cls._instance:
            cls._instance = super(University, cls).__new__(cls)
            cls._instance.university_name = university_name
            cls._instance.departments = []
            cls._instance.students = []
            cls._instance.faculty = []
            cls._instance.total_revenue = 0
            cls._instance.total_expenses = 0
        return cls._instance
    
    def add_department(self, department):
        self.departments.append(department)
    
    def register_student(self, student):
        self.students.append(student)
        self.total_revenue += 5000  
    
    def register_faculty(self, faculty):
        self.faculty.append(faculty)
        self.total_expenses += faculty.salary
    
    def calculate_finances(self):
        return f"Total Revenue: {self.total_revenue}, Total Expenses: {self.total_expenses}"



faculty1 = Faculty("abc", 45, "abc@gmail.com", "01", "CSE", 70000)
faculty2 = Faculty("xyz", 50, "xyz@gmail.com", "02", "ECE", 75000)


student1 = Student("A", 22, "a@gmail.com", "S01", "Computer Science")
student2 = Student("B", 21, "b@gmail.com", "S02", "Physics")

course1 = Course("C1", "Introduction to Computer Science", 3)
course2 = Course("P1", "Introduction to Physics", 3)

course1.add_student(student1)
course2.add_student(student2)

course1.assign_faculty(faculty1)
course2.assign_faculty(faculty2)


student1.enroll_course(course1)
student2.enroll_course(course2)


cs_department = Department("D1", "Computer Science")
phy_department = Department("D2", "Physics")


cs_department.add_student(student1)
cs_department.add_faculty(faculty1)
phy_department.add_student(student2)
phy_department.add_faculty(faculty2)

cs_department.courses_offered.append(course1)
phy_department.courses_offered.append(course2)


university = University("KL University")
university.add_department(cs_department)
university.add_department(phy_department)

university.register_student(student1)
university.register_student(student2)
university.register_faculty(faculty1)
university.register_faculty(faculty2)


print("\nDepartment Details:")
cs_department.display_details()

print("\nStudent Details:")
student1.display_details()

print("\nProfessor Details:")
faculty1.display_details()

print("\nCourse Details:")
course1.display_details()

print("\nUniversity Finances:")
print(university.calculate_finances())
