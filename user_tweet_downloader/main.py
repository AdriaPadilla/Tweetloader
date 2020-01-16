import tweet_download as td
import argparse

#screen_user_name = ['adriapadilla'] # The visual user name in twitter
#user_id = ['72066060'] # The user ID (You can use this: http://gettwitterid.com/)

# Important: Rate limit for  GET statuses/user_timeline is limited to 1800 request for a 15 min. window.

user_ids = []
usernames = []

def retrieve_info(user_ids, usernames):
    for userid, username in zip(user_ids, usernames):
        td.tweet_retrieve(userid, username)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to retrieve information about last tweets')
    parser.add_argument('--name',  type=str, nargs="+", help='user name')
    parser.add_argument('--id',  type=str,  nargs="+", help='user id')
    args = parser.parse_args()
    username = args.name
    retrieve_info(args.id, args.name)

