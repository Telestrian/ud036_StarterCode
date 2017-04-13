import webbrowser


class Movie:
    """
    This class is used to define the attributes of a movie for use in the website
    """

    # specifies the Movie class for use in the website

    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

