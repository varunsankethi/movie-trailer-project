import webbrowser

"""Class describing the attributes of a movie and 
	URLs to its poster image and youtube trailer"""

class Movie():
    """ This class provides movie details. The show_trailer() method open
    a popup window and plays the trailer"""

    def __init__(self, movie_title, 
    	movie_storyline, poster_youtube, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_youtube
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
