from Lab_1_TMPS.domain.book import Genre

class GenreFactory:
    @staticmethod
    def create_genre(genre_name):
        return Genre(genre_name)
