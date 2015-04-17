import tmdb
tmdb.configure('1c6135d99f14875c640c4859a5f7b01b')
# Search for movie titles containing "Alien"
movies = tmdb.Movies("Alien")
for movie in movies.iter_results():
    # Pick the movie whose title is exactly "Alien"
    if movie["title"] == "Alien":
        # Create a Movie object, fetching details about it
        movie = tmdb.Movie(movie["id"])
        break
# Access the fetched information about the movie
print(movie.get_title())