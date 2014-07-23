# coding: utf-8

from movie_info.models import Movie, Genre, Country, Language, Director
from crawler import fill_db_movie_info, update_csv_file
import sqlite3

### HERE YOU CHANGE FOR THE PATH WHERE test_subdataset.csv IS LOCATED ON YOUR PC ###
PATH = '/home/kiko/Downloads/DATASETS/'

if __name__ == '__main__':
	while True:
		try:
			update_csv_file(PATH + "test_subdataset_engagement2.csv", PATH + "test_subdataset_engagement3.csv")
		except:
			continue
		
	#fill_db_movie_info(PATH + "training_subdataset_engagement2.csv")