import webbrowser

"""Class describing the attributes of a movie and
URLs to its poster image and youtube trailer"""


class Movie():
    """Constructror function for class Movie
    This initializes the title, storyline,
    porter url and the trailer url"""

    def __init__(self, movie_title, movie_storyline, poster_youtube,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_youtube
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The show_trailer function will open
        a webbrowser and play the trailer in the link"""
        webbrowser.open(self.trailer_youtube)
