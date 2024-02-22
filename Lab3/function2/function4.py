from db import movies

def get_movie_with_avg_imdb(movies_list):
    count_of_movie = len(movies_list)
    all_imdb_scores = 0

    for name_of_movie in movies_list:
        for movie in movies:
            if name_of_movie.lower() == movie['name'].lower():
                all_imdb_scores += movie['imdb']
                break
    return f'avarage imdb score is: {all_imdb_scores / count_of_movie}'


print(get_movie_with_avg_imdb(['dark knight', 'hitman']))