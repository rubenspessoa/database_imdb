# coding: utf-8

from movie_info.models import Movie, Genre, Country, Language, Director
from crawler import fill_db_movie_info

### HERE YOU CHANGE FOR THE PATH WHERE test_subdataset.csv IS LOCATED ON YOUR PC ###
PATH = '/Users/rubenspessoa/Documents/Workspace/DATASET/'

if __name__ == '__main__':
	while True:
		try:	
	    	fill_db_movie_info(PATH + 'test_subdataset.csv')
	    except:
	    	continue