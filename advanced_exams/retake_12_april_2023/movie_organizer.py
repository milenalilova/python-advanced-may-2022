def movie_organizer(*args):
    movies_dict = {}
    for movie_name, genre in args:
        if genre not in movies_dict.keys():
            movies_dict[genre] = []
        movies_dict[genre].append(movie_name)
    sorted_movies_dict = dict(sorted(movies_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ''

    for gen, movies in sorted_movies_dict.items():
        output += f"{gen} - {len(movies)}\n"
        for mov in sorted(movies):
            output += f"* {mov}\n"

    return output.strip()


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print()
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
