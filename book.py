
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    def author_info(self):
        return f"{self.name}, {self.nationality}"

class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author
    
    def book_info(self):
        return f"Book: {self.title}, Author: {self.author.author_info()}"
