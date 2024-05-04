class Film:
    def __init__(self, film_id, title, director, release_year, archived=False):
        self.film_id = film_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.archived = archived