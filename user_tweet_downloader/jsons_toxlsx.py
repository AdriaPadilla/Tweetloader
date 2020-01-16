import json
import pandas as pd
import glob
import os

def get_the_data(file, screen_user_name, all_the_data, output_folder):

	the_data, tweet_date_list, tweet_text_list, tweet_retweet_count_list, fav_count_list, is_media_list, is_reply_list, hashtags_list_glob, mentions_list_glob, original_tweet_list, media_type_list = all_the_data

	with open(file) as f:
		data = json.load(f)
		for tweet in data:

		# Basic Data section
			the_data['tweet_date'] = tweet['created_at']
			try:
				the_data['tweet_text'] = tweet['text']
			except KeyError:
				the_data['tweet_text'] = "empty"

			the_data['retweet_count'] = tweet['retweet_count']
			the_data['fav_count'] = tweet['favorite_count']

		# Media Section
			try:
				the_data['is_media'] = tweet['entities']['media'][0]['media_url_https']
			except KeyError:
				the_data['is_media'] = "null"
			try:
				the_data['media_type'] = tweet['entities']['media'][0]['type']
			except KeyError:
				the_data['media_type'] = "null"

		# Reply Section
			try:
				the_data['is_reply'] = tweet['in_reply_to_screen_name']
			except KeyError:
				the_data['is_reply'] = "null"

		# User Mentions section
			user_mentions = tweet['entities']['user_mentions']
			user_mentions_list = []
			if user_mentions:
				for mention in user_mentions:
						user_mentions_list.append(mention['screen_name'])
				the_data['mentions_in_text'] = ",".join(user_mentions_list)
			else:
				the_data['mentions_in_text'] = "null"

		# Hashatgs section
			hashtags = tweet['entities']['hashtags']
			hashtags_in_text_list = []
			if hashtags:
				for element in hashtags:
					hashtags_in_text_list.append(element['text'])
				the_data['hashtags_in_text'] = ",".join(hashtags_in_text_list)
			else:
				the_data['hashtags_in_text'] = "null"

		# If retweet == True -> original tweet date
			try:
				the_data['original_tweet_date'] = tweet['retweeted_status']['created_at']
			except KeyError:
				the_data['original_tweet_date'] = "null"

		# From dictionary to list
			tweet_text_list.append(the_data["tweet_text"])
			tweet_date_list.append(the_data["tweet_date"])
			tweet_retweet_count_list.append(the_data['retweet_count'])
			fav_count_list.append(the_data['fav_count'])
			is_reply_list.append(the_data['is_reply'])
			is_media_list.append(the_data['is_media'])
			hashtags_list_glob.append(the_data['hashtags_in_text'])
			mentions_list_glob.append(the_data['mentions_in_text'])
			original_tweet_list.append(the_data['original_tweet_date'])
			media_type_list.append(the_data['media_type'])

		# creating Dataframe from lists
		df = pd.DataFrame({
			"date":tweet_date_list,
			"retweet_count": tweet_retweet_count_list,
			"fav_count": fav_count_list,
			"in_reply": is_reply_list,
			"hashtags": hashtags_list_glob,
			"mentions": mentions_list_glob,
			"text":tweet_text_list,
			"media_type": media_type_list,
			"is_media":is_media_list,
			"original_tweet_date":original_tweet_list,
			})

		# Export Dataframe
		output_file = os.path.join(output_folder, screen_user_name, screen_user_name + ".xlsx")
		df.to_excel(output_file)
		return output_file


def convert_all(save_path, screen_user_name, output_folder):
	json_files = glob.glob(os.path.join(save_path, "*.json"))

	the_data = {}
	tweet_date_list = []
	tweet_text_list = []
	tweet_retweet_count_list = []
	fav_count_list = []
	is_media_list = []
	is_reply_list = []
	hashtags_list_glob = []
	mentions_list_glob = []
	original_tweet_list = []
	media_type_list = []

	all_the_data =	[
					the_data, tweet_date_list, tweet_text_list, tweet_retweet_count_list,
					fav_count_list, is_media_list, is_reply_list, hashtags_list_glob,
					mentions_list_glob, original_tweet_list, media_type_list
					]


	for json_file in json_files:
		output_file = get_the_data(json_file, screen_user_name, all_the_data, output_folder)

	# When loop ends
	print("File created: " + screen_user_name + ".xlsx")
	return output_file

"""
	# Clear all lists and dicts in each loop
	the_data.clear()
	tweet_date_list.clear()
	tweet_text_list.clear()
	tweet_retweet_count_list.clear()
	fav_count_list.clear()
	is_media_list.clear()
	is_reply_list.clear()
	hashtags_list_glob.clear()
	mentions_list_glob.clear()
	original_tweet_list.clear()
	media_type_list.clear()
"""