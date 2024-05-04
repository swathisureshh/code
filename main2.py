from film import Film
from film_archive import FilmArchive
from researcher import Researcher

archive = FilmArchive()
archive.add_film(Film(1, "Casablanca", "Michael Curtiz", 1942))
archive.add_film(Film(2, "Gone with the Wind", "Victor Fleming", 1939, True))
archive.add_film(Film(3, "Kesari", "Anurag Singh", 2019))
archive.add_film(Film(4, "Mangal Pandey", "Ketan Mehta", 2001))
archive.add_film(Film(5, "Padmaavat", "Leela Bhansali", 2018, True))

researcher1 = Researcher(6534, "anu", "password123")
researcher2 = Researcher(1234, "swathi", "password456")
researcher3 = Researcher(7891, "nayana", "password789")
researcher4 = Researcher(3421, "anupama", "password321")

archive.add_researcher(researcher1)
archive.add_researcher(researcher2)
archive.add_researcher(researcher3)
archive.add_researcher(researcher4)

user_type = input("Are you a regular user or a researcher? (Type 'user' or 'researcher'): ").lower()

if user_type == 'researcher':
    researcher_name = input('Enter your researcher name: ')
    researcher_password = input('Enter your researcher password: ')
    if archive.authenticate_researcher(researcher_name, researcher_password):
        print('Authentication successful Welcome researcher.')
        researcher = next((r for r in archive.researchers if r.name == researcher_name), None)
        
        film_id_to_update = int(input("Enter the ID of the movie you want to update: "))
        updated_title = input("Enter updated title: ")
        updated_director = input("Enter updated director: ")
        updated_release_year = int(input("Enter updated release year: "))
        updated_archived = input("Is the movie archived? (True/False): ").lower() == 'true'
        updated_movie = Film(film_id_to_update, updated_title, updated_director, updated_release_year, updated_archived)
        
        archive.update_film(researcher, film_id_to_update, updated_movie)
        
        film_id_to_delete = int(input("Enter the ID of the movie you want to delete: "))
        archive.delete_film_by_researcher(researcher, film_id_to_delete)
    else:
        print('Invalid researcher credentials.')
elif user_type == 'user':
    normal_movies = archive.get_normal_movies()
    print("Normal Movies:")
    for film in normal_movies:
        print(f"Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")
else:
    print('Invalid user type.')