'''
Movie Class with Rating
•	Create a class called Movie with attributes:
        o	title: Title of the movie.
        o	genre: Genre of the movie.
        o	rating: IMDb rating of the movie.
•	Write methods to:
        o	Display movie details.
        o	Check if the movie rating is above 8 (considered “highly rated”).
•	Create instances of Movie and test these methods.
'''

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def display_details(self):
        print(f"Title: {self.title}\nGenre: {self.genre}\nIMDb Rating: {self.rating}")

    def is_highly_rated(self):
        if self.rating > 8:
            print(f"{self.title} is a highly rated movie!")
        else:
            print(f"{self.title} is not a highly rated movie.")

m1 = Movie("Inception", "Sci-Fi", 8.8)
m2 = Movie("Business Proposal", "Drama", 3.7)
m3 = Movie("Joker", "Adventure", 9.0)
m4 = Movie("Venom: the last dance", "Action", 7.0)

m1.display_details()
m1.is_highly_rated()

print("")

m2.display_details()
m2.is_highly_rated()

print("")

m3.display_details()
m3.is_highly_rated()

print("")

m4.display_details()
m4.is_highly_rated()