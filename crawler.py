# coding: utf-8

from movie_info.models import Movie, Genre, Director, Language, Country

def get_movie_info(codigo_do_filme):
    import imdb
    ia = imdb.IMDb()
    movie = ia.get_movie(codigo_do_filme)
    dic_return = {}
    
    if movie.has_key('title'):
        dic_return['titulo'] = movie['title']
    if movie.has_key('rating'):
        dic_return['rating'] = movie['rating']
    if movie.has_key('votes'):
        dic_return['votes'] = movie['votes']
    if movie.has_key('year'):
        dic_return['ano'] = movie['year']
    if movie.has_key('genre'):
        dic_return['genero'] = movie['genre'][0]
    if movie.has_key('countries'):
        dic_return['pais'] = movie['countries'][0]
    if movie.has_key('lang'):
        dic_return['idioma'] = movie['lang'][0]
    if movie.has_key('director'):
        dic_return['directors'] = movie['director']
    
    return dic_return 

def read_sheet(file_name, fieldnames=None, delimiter=",", quotechar="\n"):
    from csv import DictReader
    reader = DictReader(open(file_name, 'rb'), fieldnames=fieldnames, delimiter=delimiter, quotechar=quotechar)
    return reader

def save_sheet(file_name, content, title):        
    import csv
    csv_writer = csv.writer(open(file_name, 'wb'))
    csv_writer.writerow(title)
    for c in content:
        csv_writer.writerow(c)

def fill_db_movie_info(the_sheet_file):
    file_csv = read_sheet(the_sheet_file)
    
    for movie in file_csv:
        try:
            id_filme = file_csv['id_move']
            
            if not Movie.objects.filter(id_movie=id_filme).exists():
                
                info = get_movie_info(id_filme)
                
                if info.has_key('rating'):
                    rating_imdb = info['rating']
                else:
                    rating_imdb = -1
                    
                if info.has_key('votes'):
                    movie_votes = info['votes']
                else:
                    movie_votes = -1
                    
                if info.has_key('ano'):
                    movie_year = info['ano']
                else:
                    movie_year = -1
                
                addToDB = Movie(id_filme, rating_imdb, movie_votes, movie_year)
                addToDB.save()
                
                if info.has_key('genero'):
                    
                    movie_genre = info['genero']
                    genreToDB, created = Genre.objects.get_or_create(genre=movie_genre)
                    addToDB.genre.add(genreToDB)
                    
                if info.has_key('pais'):
                    
                    movie_country = info['pais']
                    countryToDB, created = Country.objects.get_or_create(country=movie_country)
                    addToDB.country.add(countryToDB)
                    
                if info.has_key('idioma'):
                    
                    movie_lang = info['idioma']
                    langToDB, created = Language.objects.get_or_create(language=movie_lang)
                    addToDB.language.add(langToDB)
                      
                if info.has_key('directors'):
                    
                    movie_directors = info['directors']
                    
                    for m_director in movie_directors:
                        directorToDB, created = Director.objects.get_or_create(director=m_director['name'])
                        addToDB.directors.add(directorToDB)
        except:
            continue
                    
def update_csv_file(the_sheet_file, output_file):
    import sys
    encode = sys.stdin.encoding
    file_csv = read_sheet(the_sheet_file)
    
    title = ['id_movie', 'movie_rating', 'crawled_time', 'tweet_time', 'followers_count', 'statuses_count',
             'favourites_count', 'engagement', 'imdb_rating', 'imdb_votes_count',
             'movie_year', 'movie_country', 'movie_director', 'movie_genre', 'movie_language']
    content = []
    
    for movie in file_csv:
       
        id_movie = movie["id_move"].encode(encode)
        movie_rating = movie["movie_rating"].encode(encode)
        crawled_time = movie["crawled_time"].encode(encode)
        tweet_time = movie["tweet_time"].encode(encode)
        followers_count = movie['followers_count'].encode(encode)
        statuses_count = movie['statuses_count'].encode(encode)
        favourites_count = movie['favourites_count'].encode(encode)
        engagement = movie['engagement'].encode(encode)
        
        row = [id_movie, movie_rating, crawled_time, tweet_time, followers_count, statuses_count, favourites_count,
               engagement]
        
        if Movie.objects.filter(id_movie=movie["id_move"]).exists():
            
            movie_obj = Movie.objects.get(id_movie=movie["id_move"])
            
            row.append(movie_obj.rating)
            row.append(movie_obj.votes)
            row.append(movie_obj.year)
            
            if movie_obj.country.exists():
                row.append(movie_obj.country.all())
            else:
                row.append(-1)
            
            if movie_obj.directors.exists():
                row.append(movie_obj.directors.all())
            else:
                row.append(-1)
                
            if movie_obj.genre.exists():
                row.append(movie_obj.genre.all())
            else:
                row.append(-1)
    
            if movie_obj.language.exists():
                row.append(movie_obj.language.all())
            else:
                row.append(-1)

        content.append(row)
    save_sheet(file_name=output_file, content=content, title=title)
