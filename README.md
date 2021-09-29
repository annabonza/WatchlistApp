"""

WATCHLIST APP

"""

A multiple user app.

app.py - user interaction file

database.py - containing queries, and functions allowing to interact with the database

Functionalities:
- adding a movie to your list
- view upcoming movies
- view all movies on your list
- check off a movie after watching
- view list of all watched movies
- add users
- search for a movie to watch.

Index branch contains an index created on release_timestamp. 
The speed will be unnoticeable, though for this size of app.
In case of the movies table getting large, with a lot of rows an index will speed up the search.
