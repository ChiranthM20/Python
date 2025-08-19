'''Create a Class with a Constructor:

Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie's title and rating.'''



class Movie:
    def __init__(self, title, rating):
        self.title=title
        self.rating=rating
        
    def display(self):
        print(f"I love {self.title} movies and all the movies of {self.title} has the rating above {self.rating}")

Thor = Movie("Thor", "9")
IronMan = Movie("IronMan", "9.2")

Thor.display()
IronMan.display()

