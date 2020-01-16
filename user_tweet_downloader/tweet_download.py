from TwitterAPI import TwitterAPI
import json
import time
import os
import user_tweet_downloader.jsons_toxlsx as to_xlsx

def tweet_retrieve(user_id, screen_user_name):
	print("Connecting Twitter API and retrieving Tweets from " + screen_user_name + "  (Please Wait!)")
	output_folder = "output"
	save_path = os.path.join(output_folder, screen_user_name)

	if not os.path.exists(save_path):
		os.makedirs(save_path)

	count_id = 0
	all_tweets = []
	jsons = []
	first_search = True

	while count_id < 3200: # Limit is 3200. 200 is the limit by query.
		if first_search:
			tweets = api.request('statuses/user_timeline', {'user_id': user_id, 'screen_name': screen_user_name, 'count': '200'})
			first_search = False
		else:
			tweets = api.request('statuses/user_timeline', {'user_id': user_id, 'screen_name': screen_user_name, 'count': '200', 'max_id': last_id})
		json_info = tweets.json()
		last_id = json_info[-1]["id"]
		all_tweets.append(tweets)
		count_id += 200

	for i, tweet in enumerate(all_tweets):
		json_tweets = tweet.json()
		if first_search:
			pass
		else:
			json_tweets = json_tweets[1:]
		
		timestr = time.strftime("%Y%m%d-%H%M") # Get the actual time to use as part of file name
		timestr2 = time.strftime("%Y-%m-%d/%H:%M:%S") # Get the time to know when is executed

# Now save the json files
		file_name = screen_user_name+timestr+"_"+str(i)+"_.json"
		jsons.append(os.path.join(save_path, file_name))
		with open(os.path.join(save_path, file_name), "w") as write_file:
			json.dump(json_tweets, write_file, sort_keys=True, indent=4) 
			print("Response downloaded on: "+timestr2+" | Filename: "+file_name)

# Import json to xlsx conversion script
	if count_id == 3200:
		print("Creating " + screen_user_name + ".xlsx (This could take a while...)")
		to_xlsx.convert_all(save_path, screen_user_name, output_folder)
		print("Job done!")
	return jsons


## Twitter KEYS

consumer_key = "D6Rho8EtlSKprpNmChXCSXtK6"
consumer_secret = "Xa56KMvmYI0VisN5aeJvjPzJiONzheMIXCQ3aQa4em4bWdxCSG"
access_token_key = "72066060-yHaMM49SeDtYApVNHTTvHZ3SaRlT5ijQqZqxnPGHY"
access_token_secret = "3EQ6QqU2qzJ1YNNOT1eVYbC7aImkgWUzpUZ1kAEFWvD6t"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


