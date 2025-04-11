from vehicle import SchoolBus
from employee import Employee
from school import SchoolOne, SchoolTwo
from vector import Vector
from book import Author, Book

# SchoolBus example
school_bus = SchoolBus("Ford", "Transit", 2021, 50)
print(school_bus.is_instance_of_vehicle())

# Employee examples
employee1 = Employee("John", 30)
employee2 = Employee("Jane", 28, "Manager", 50000)
print(employee1)
print(employee2)

# School examples
students_one = [
    {"name": "Alice", "grade": 85, "gpa": 3.5},
    {"name": "Bob", "grade": 90, "gpa": 3.8},
]
students_two = [
    {"name": "Charlie", "grade": 88, "gpa": 3.6},
    {"name": "David", "grade": 92, "gpa": 3.9},
]

school_one = SchoolOne(students_one)
school_two = SchoolTwo(students_two)

school_one.display_info()
school_two.display_info()

# Vector example
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
result_vector = vector1 + vector2
print("Resultant Vector:", result_vector)

# Book and Author example
author = Author("J.K. Rowling", "British")
book = Book("Harry Potter and the Philosopher's Stone", author)
print(book.book_info())
