class FilmArchive:
    def __init__(self):
        self.film_records = []
        self.researchers = []

    def add_film(self, film):
        self.film_records.append(film)

    def delete_film(self, film_id):
        for film in self.film_records:
            if film.film_id == film_id:
                self.film_records.remove(film)
                break
        else:
            print(f"Film with ID {film_id} not found in the archive.")

    def update_film(self, researcher, film_id, updated_data):
        if researcher in self.researchers:
            for film in self.film_records:
                if film.film_id == film_id:
                    film.title = updated_data.title
                    film.director = updated_data.director
                    film.release_year = updated_data.release_year
                    film.archived = updated_data.archived
                    print("Film updated successfully!")
                    print("\nUpdated List of Movies:")
                    for film in self.film_records:
                        print(f"Film ID: {film.film_id}, Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}, Archived: {film.archived}")
                    
                    archived_movies = self.get_archived_movies()
                    print("\nArchived Movies:")
                    for film in archived_movies:
                        print(f"Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")
                    
                    return
            print(f"Film with ID {film_id} not found in the archive.")
        else:
            print("Only authenticated researchers can update films.")

    def get_film_details(self, film_id):
        for film in self.film_records:
            if film.film_id == film_id:
                return f"Film ID: {film.film_id}\nTitle: {film.title}\nDirector: {film.director}\nRelease Year: {film.release_year}"
        return f"Film with ID {film_id} not found in the archive."

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def delete_researcher(self, researcher_id):
        for researcher in self.researchers:
            if researcher.id == researcher_id:
                self.researchers.remove(researcher)
                break
        else:
            print(f"Researcher with ID {researcher_id} not found.")

    def authenticate_researcher(self, name, password):
        for researcher in self.researchers:
            if researcher.name == name and researcher.password == password:
                return True
        return False

    def get_normal_movies(self):
        return [film for film in self.film_records if not film.archived]

    def get_archived_movies(self):
        return [film for film in self.film_records if film.archived]

    def delete_film_by_researcher(self, researcher, film_id):
        if researcher in self.researchers:
            for film in self.film_records:
                if film.film_id == film_id:
                    self.film_records.remove(film)
                    print(f"Film with ID {film_id} has been successfully deleted.")
                    return
            print(f"Film with ID {film_id} not found in the archive.")
        else:
            print("Only authenticated researchers can delete films.")

