"""
Cel mai vizionat film - Fight Club in cazul de mai sus

Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...

Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
"""

x = [
    {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
    {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
    {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionaire']}
]

# Cel mai vizionat film
all_movies = []
for person in x:
    for movie in person['filme']:
        all_movies.append(movie)

most_watched = ''
max_count = 0
for movie in all_movies:
    count = 0
    for m in all_movies:
        if m == movie:
            count += 1
    if count > max_count:
        max_count = count
        most_watched = movie

print(f'Cel mai vizionat film este {most_watched}')

# Utilizatorul cu cele mai multe filme vizionate
max_movies = 0
max_movies_user = ''
for person in x:
    if len(person['filme']) > max_movies:
        max_movies = len(person['filme'])
        max_movies_user = person['nume']

print(f"Utilizatorul cu cele mai multe filme vizionate este {max_movies_user} cu {max_movies} filme.")

# Top filme dupa vizionari
unique_movies = []
for movie in all_movies:
    if movie not in unique_movies:
        unique_movies.append(movie)

movie_counts = []
for movie in unique_movies:
    count = 0
    for m in all_movies:
        if m == movie:
            count += 1
    movie_counts.append((movie, count))

# Sort movies by count (bubble sort)
n = len(movie_counts)
for i in range(n):
    for j in range(0, n-i-1):
        if movie_counts[j][1] < movie_counts[j+1][1]:
            movie_counts[j], movie_counts[j+1] = movie_counts[j+1], movie_counts[j]

print("Top filme dupa vizionari:")
for movie, count in movie_counts:
    print(f"{movie}: {count}")

# Top utilizatori cu cele mai multe filme vizionate
user_movies = []
for person in x:
    user_movies.append((person['nume'], len(person['filme'])))

# Sort users by movie count (bubble sort)
n = len(user_movies)
for i in range(n):
    for j in range(0, n-i-1):
        if user_movies[j][1] < user_movies[j+1][1]:
            user_movies[j], user_movies[j+1] = user_movies[j+1], user_movies[j]

print("\nTop utilizatori cu cele mai multe filme vizionate:")
for user, count in user_movies:
    print(f"{user}: {count}")