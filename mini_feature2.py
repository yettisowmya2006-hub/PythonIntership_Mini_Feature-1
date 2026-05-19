movies = ["Leo", "RRR", "Pushpa", "Kalki"]

ratings = []

print("Movie List:")
for index, movie in enumerate(movies):
    print(index, ":", movie)

for movie in movies:
    rate = int(input(f"Enter rating for {movie} (1-5): "))
    ratings.append(rate)

highest = max(ratings)
lowest = min(ratings)
average = sum(ratings) / len(ratings)

print("\n--- Movie Report ---")

for i in range(len(movies)):
    print(movies[i], "=", ratings[i], "stars")

print("\nHighest Rating:", highest)
print("Lowest Rating:", lowest)
print("Average Rating:", average)