import math

class Rating:
	def __init__(self, user_id, movie_id, rating):
		self.user_id = user_id
		self.movie_id = movie_id
		self.rating = rating

class Similarity:
	def __init__(self, user_source_id, user_target_id, similarity):
		self.user_source_id = user_source_id
		self.user_target_id = user_target_id
		self.similarity = similarity

def watched_movie_ids_for(user_id):
	return [rating.movie_id for rating in ratings if rating.user_id == user_id]

def interset(array1, array2):
	return list(set(array1).intersection(array2))

def user_rating_for_movie(user_id, movie_id):
	for rating in ratings:
		if rating.user_id == user_id and rating.movie_id == movie_id:
			return rating.rating

def top_k_neighbour_for(user_id, k, similarities):
	remaining_seat = k
	for similarity in similarities:
		

# split file
ratings_file = open('ratings.txt', 'r')
traning_set = open('traning_set.txt', 'w')
testing_set = open('testing_set.txt', 'w')
ratings = []
similarities = []
user_id = 0
user_ids = []
for line in ratings_file:
	rating = line.split('::')
	if user_id == rating[0]:
		traning_set.write(line)
		ratings.append(Rating(user_id, rating[1], rating[2]))
		user_ids.append(user_id)
	else:
		user_id = rating[0]
		testing_set.write(line)

user_ids = ['1', '2', '3', '4']
for source_user_id in user_ids:
	source_user_watched_movie_ids = watched_movie_ids_for(source_user_id)
	user_ids.remove(source_user_id)

	for target_user_id in user_ids:
		target_user_watched_movie_ids = watched_movie_ids_for(target_user_id)
		intersection_movie_ids = interset(source_user_watched_movie_ids, target_user_watched_movie_ids)

		similarity = 0
		for movie_id in intersection_movie_ids:
			source_user_rating = user_rating_for_movie(source_user_id, movie_id)
			target_user_rating = user_rating_for_movie(target_user_id, movie_id)
			similarity += math.pow(abs(int(source_user_rating) - int(target_user_rating)), 2)

		print similarity
		similarities.append(Similarity(source_user_id, target_user_id, math.sqrt(similarity)))
