movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

while True:
    response = input("Do you want to add a movie? (yes/no): ")
    if response.lower() == "yes":
        name = input("Enter the movie name: ")
        budget = int(input("Enter the movie budget: "))
        movies.append((name, budget))
    else:
        break

high_budget_movies = []
total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

for movie in movies:
    if movie[1] > average_budget:
        high_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(f"Movie: {movie[0]} cost: ${movie[1]:,}: ${over_average_cost:,} over average")

print(f"There were {len(high_budget_movies)} movies with over average budget.")
