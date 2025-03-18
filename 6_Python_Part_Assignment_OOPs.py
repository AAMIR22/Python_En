# Question 1: (5 Marks)
# Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
# course_code: a string representing the course code (e.g., "CS101")
# course_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3)
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
# ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        status = "Required" if self.required_for_major else "Not Required"
        return f"{super().__str__()}, Required for Major: {status}"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"{super().__str__()}, Elective Type: {self.elective_type}"

# Example usage
core = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective = ElectiveCourse("ART200", "Painting Basics", 2, "Liberal Arts")

print("\n1) University's course catalogue:")
print(core)
print(elective)
print()


# Question 2: (5 Marks)
# Create a Python module named employee that contains a class Employee with attributes
# name, salary and methods get_name() and get_salary().
# Write a program to use this module to create an object of the Employee class and display its name and salary.




from Python_employee_module import Employee
#from file Python_employee_module

# Create an Employee object
employee = Employee("Aamir", 100000)

# Display the employee's details
print("\n2) Employee:")
print(f"Name: {employee.get_name()}")
print(f"Salary: {employee.get_salary()}")
