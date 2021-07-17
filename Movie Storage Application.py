MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ").title()
    director = input("Enter the movie director: ").title()
    year = input("Enter the movie release year: ").title()

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"\nTitle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    search_title = input("Enter the movie title you are looking for: ").title()

    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)
            break
    else:
        print(f"The movie {search_title} is not on the database.")


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
