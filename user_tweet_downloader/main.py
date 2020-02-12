import argparse
import user_tweet_downloader.tweet_download as td

# Usernames = ['adriapadilla'] # The visual user name in twitter
# User_ids = ['72066060'] # The user ID (You can use this: http://gettwitterid.com/)
# Extraction Example: python3 -m user_tweet_downloader.main --username adriapadilla --id 72066060

# Important: Rate limit for  GET statuses/user_timeline is limited to 1800 request for a 15 min. window.

# Instructions for Big queries
# Put User ID (numbers) in user_ids Variable
# Put User visible names (without "@") in usernames Variable
# Eache ID and User_name must be betweet " ", and separated by comas (see example).
# IMPORTANT: You must follow the same order in IDs and User_names!
# You can find user ID's here: http://gettwitterid.com

# Example: 
"""
user_ids = ["72066060", "second_id", "third_id"]
usernames = ["adriapadilla", "second_username", "third_username"]

"""

user_ids = []
usernames = []

def retrieve_info(userid, username):
    for userid, username in zip(user_ids, usernames):
        td.tweet_retrieve(userid, username)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to retrieve information about last tweets')
    parser.add_argument('--name',  type=str, nargs="+", help='user name')
    parser.add_argument('--id',  type=str,  nargs="+", help='user id')
    args = parser.parse_args()
    username = args.name
    retrieve_info(args.id, args.name)

