# coding: utf-8

from movie_info.models import Movie, Genre, Country, Language, Director
from crawler import fill_db_movie_info, update_csv_file

### HERE YOU CHANGE FOR THE PATH WHERE test_subdataset.csv IS LOCATED ON YOUR PC ###
PATH = '/Users/rubenspessoa/Documents/Workspace/database_IMDb_v2/DATASETS/'

if __name__ == '__main__':
	#fill_db_movie_info(PATH + "training_subdataset_engagement2.csv")
	#update_csv_file(PATH + "test_subdataset_engagement2.csv", PATH + "test_subdataset_engagement3.csv")
	
		
	