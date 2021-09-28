import datetime
import database

welcome = "Create your own watchlist"

menu = """Please select one of below options:
1) Add Movie
2) Upcoming Movies
3) View All
4) Check Off
5) Watched Movies
6) Add User
7) Search
8) Exit

Your selection: """


def prompt_add_movie():
	"""
	strptime - parsing string into date time
	"""
	title = input("Movie title: ")
	release_date = input("Release date (dd-mm-yyyy): ")
	parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
	timestamp = parsed_date.timestamp()

	database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
	print(f"-- {heading} movies --")
	for movie in movies:
		movie_date = datetime.datetime.fromtimestamp(movie[2])
		full_date = movie_date.strftime("%d %b %Y")
		print(f"{movie[0]}: {movie[1]} on {full_date}")
	print("---- \n")


def prompt_watched_movie():
	username = input("Username: ")
	movie_id = input("Movie ID: ")
	database.watched_movie(username, movie_id)


def prompt_add_user():
	username = input("Username: ")
	database.create_users(username)


def prompt_show_watched_movies():
	username = input("Username: ")
	movies = database.get_watched_movies(username)
	if movies:
		print_movie_list(f"Watched", movies)
	else:
		print("That user has watched no movies yet.")


def prompt_search_movies():
	search_term = input("What do you want to watch? ")
	movies = database.search_movies(search_term)
	if movies:
		print_movie_list("Found", movies)
	else:
		print("Found no movies for that search term.")


def main():
	print(welcome)
	database.create_tables()
	user_input = input(menu)

	while user_input != "8":
		if user_input == "1":
			prompt_add_movie()
		elif user_input == "2":
			movies = database.get_movies(True)
			print_movie_list("Upcoming", movies)
		elif user_input == "3":
			movies = database.get_movies()
			print_movie_list("All", movies)
		elif user_input == "4":
			prompt_watched_movie()
		elif user_input == "5":
			prompt_show_watched_movies()
		elif user_input == "6":
			prompt_add_user()
		elif user_input == "7":
			prompt_search_movies()
		else:
			print("Invalid input. Please try again!")

		user_input = input(menu)


if __name__ == '__main__':
	main()
