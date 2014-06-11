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
    reader = DictReader(open(file_name,'rb'), fieldnames = fieldnames, delimiter = delimiter, quotechar=quotechar)
    return reader

def fill_db_movie_info(the_sheet_file):
    file_csv = read_sheet(the_sheet_file)
    
    for movie in file_csv:

        id_filme = movie['id_move']
        
        if not Movie.objects.filter(id_movie=id_filme).exists():
            
            info = get_movie_info(id_filme)
            list_to_print = list()
            list_to_print.append(id_filme)

            if info.has_key('rating') and info.has_key('votes') and info.has_key('ano'):
                rating_imdb = info['rating']
                movie_votes = info['votes']
                movie_year = info['ano']
                list_to_print.append(rating_imdb)
                list_to_print.append(movie_votes)
                list_to_print.append(movie_year)
                addToDB = Movie(id_filme, rating_imdb, movie_votes, movie_year)
                addToDB.save()
                
                if info.has_key('genero'):
                    
                    movie_genre = info['genero']
                    list_to_print.append(movie_genre)
                    
                    genreToDB, created = Genre.objects.get_or_create(genre=movie_genre)
                    addToDB.genre.add(genreToDB)
                    
                if info.has_key('pais'):
                    
                    movie_country = info['pais']
                    list_to_print.append(movie_country)
                    
                    countryToDB, created = Country.objects.get_or_create(country=movie_country)
                    addToDB.country.add(countryToDB)
                    
                if info.has_key('idioma'):
                    
                    movie_lang = info['idioma']
                    list_to_print.append(movie_lang)
                    langToDB, created = Language.objects.get_or_create(language=movie_lang)
                    addToDB.language.add(langToDB)
                      
                if info.has_key('directors'):
                    
                    movie_directors = info['directors']
                    
                    for m_director in movie_directors:
                        list_to_print.append(m_director['name'])
                        directorToDB, created = Director.objects.get_or_create(director=m_director['name'])
                        addToDB.directors.add(directorToDB)
                    
            print "salvou: ", list_to_print
