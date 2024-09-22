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

# Flatten the list of movies
all_movies = []
for person in x:
    for movie in person['filme']:
        all_movies.append(movie)

# Count occurrences of each movie
movie_counts = {}
for movie in all_movies:
    if movie in movie_counts:
        movie_counts[movie] += 1
    else:
        movie_counts[movie] = 1

# Convert dictionary to list of tuples
movie_count_list = []
for movie, count in movie_counts.items():
    movie_count_list.append((movie, count))

# Sort movies by count in descending order
n = len(movie_count_list)
for i in range(n):
    for j in range(0, n-i-1):
        if movie_count_list[j][1] < movie_count_list[j+1][1]:
            movie_count_list[j], movie_count_list[j+1] = movie_count_list[j+1], movie_count_list[j]

print("Top filme dupa vizionari:")
for movie, count in movie_count_list:
    print(f"{movie}: {count}")