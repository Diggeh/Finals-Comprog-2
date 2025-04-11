
class School:
    def __init__(self, students):
        self.students = students
    
    def average_grade(self):
        total_grades = sum([student["grade"] for student in self.students])
        return total_grades / len(self.students)
    
    def average_gpa(self):
        total_gpa = sum([student["gpa"] for student in self.students])
        return total_gpa / len(self.students)

class SchoolOne(School):
    def __init__(self, students):
        super().__init__(students)
    
    def display_info(self):
        print("SchoolOne Average Grade:", self.average_grade())
        print("SchoolOne Average GPA:", self.average_gpa())

class SchoolTwo(School):
    def __init__(self, students):
        super().__init__(students)
    
    def display_info(self):
        print("SchoolTwo Average Grade:", self.average_grade())
        print("SchoolTwo Average GPA:", self.average_gpa())
