import datetime
import database

welcome = "Create your own watchlist"

menu = """Please select one of below options:
1) Add Movie
2) Upcoming Movies
3) View All
4) Check Off
5) Watched Movies
6) Exit

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
		movie_date = datetime.datetime.fromtimestamp(movie[1])
		full_date = movie_date.strftime("%d %b %Y")
		print(f"{movie[0]} on {full_date}")
	print("---- \n")


def prompt_watched_movie():
	movie_title = input("Enter movie title you've watched: ")
	database.watched_movie(movie_title)


def main():
	print(welcome)
	database.create_tables()
	user_input = input(menu)

	while user_input != "6":
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
			movies = database.get_watched_movies()
			print_movie_list("Watched", movies)
		else:
			print("Invalid input. Please try again!")

		user_input = input(menu)


if __name__ == '__main__':
	main()
