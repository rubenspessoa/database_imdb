# coding: utf-8

from movie_info.models import Movie, Genre, Country, Language, Director
from crawler import fill_db_movie_info

if __name__ == '__main__':
	while True:
    	fill_db_movie_info('/Users/rubenspessoa/Documents/Workspace/DATASET/test_subdataset.csv')
    except:
    	continue