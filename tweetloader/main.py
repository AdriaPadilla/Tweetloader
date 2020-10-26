import tweet_download as td
import accounts as ac
import argparse, textwrap
import pandas as pd

users = ac.USERS # want to integrate this as API? Use account.py to define usernames
dataframes = []

def main(users, concat, j):

	print("users to retrieve: "+str(users))
	print("Selected Options")
	print("Concatenate datasets: "+str(concat))
	print("Delete JSON files: "+str(j))
	print("starting...")

	for user in users:
		user_frame = td.tweet_retrieve(user, j)
		user_frame["owner"] = user
		if concat == True:
			dataframes.append(user_frame)
		else:
			pass
	if concat == True:
		print("Creating global Dataset... Concatenate all users. Wait!!!")
		df = pd.concat(dataframes)
		df.to_excel("outputs/all_users.xlsx")
	else:
		pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description= textwrap.dedent('''\
									About: TweetLoader is a simple tool to download Tweets from user Timeline
									How it Works: This tool will create a ouput dir, with .xlxs file with data for each user
									
									Please, note actual API limitations:
									 - The latest 3200 from each user
									 - Only Native tweets
									 - Only 100.000 calls in a 24h period
									 - Request limit: 1500 requests in a 15-min window
									 - Know more: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
									 
									Developed by: Adrian Padilla (adrian.padilla@uab.cat)
									Citation APA Style: Padilla, Adrian (2020). Tweetloader (Version 2) [Software]. Avaliable from: 
									
									Usage Example: python tweetloader --u adriapadilla nitxa -c -j
									- This query will download tweets from users: adriapadilla and nitxa
									- Also, will crate a global dataset with both users
									- Will preserve original API responses in JSON format
									 '''),
									formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('--u', type=str, nargs="+", help= textwrap.dedent('''\
						Use a single user or multiple usernames 
						If Multiple users: space separated without quotes
						Example: python tweetloader --u username1 username2 -optional_args -optional_args
						
						Non-mandatory (optional) arguments:
						'''))
	parser.add_argument('-c',
						action="store_true",
						default=False,
						help="Create a single DataSet with all defined users. Disabled by default")
	parser.add_argument('-j',
						action="store_false",
						default=True,
						help="Preserve original JSON files from API Response. Deleted by default")

	args = parser.parse_args()
	users = args.u
	concat = args.c
	j = args.j

	main(users, concat, j)