from abc import ABC, abstractmethod
import random

class Media(ABC):
    def __init__(self, name: str, stars: float):
        self._name = name
        self._stars = stars

    def play(self):
        pass

class Movie(Media):
    def __init__(self, name: str, stars: float, director: str, duration: int):
        super().__init__(name, stars)

        self._director = director
        self._duration = duration

    def play(self):
        return f"{self._name} is playing now."
    
    def __str__(self):
        return f"Movie: {self._name}, Rating: {self._stars}/5, Duration: {self._duration} mins, Director: {self._director}."
    
class Song(Media):
    def __init__(self, name: str, stars: float, artist: str, album: str):
        super().__init__(name, stars)

        self._artist = artist
        self._album = album
    
    def play(self):
        return f"{self._name} is playing now."
    
    def __str__(self):
        return f"Song: {self._name}, Rating: {self._stars}/5, Artist: {self._artist} mins, Album: {self._album}."
    
# Songs
thatsAmore = Song("That's Amore", 4.7, "Dean Martin", "That's Amore")
mammaMaria = Song("Mamma Maria", 4.0, "Ricchi e Poveri", "Mamma Maria")
loseYourself = Song("Lose Yourself", 3.8, "Eminem", "8 Mile")
# Movies
interstellar = Movie("Interstellar", 4.8, "Christopher Nolan", 169)
fordVFerrari = Movie("Ford v Ferrari", 4.8, "James Mangold", 152)
tenet = Movie("Tenet", 4.0, "Christopher Nolan", 150)


playlist = [thatsAmore, mammaMaria, loseYourself, interstellar, fordVFerrari, tenet]

print((playlist[random.randint(0,5)]).play())