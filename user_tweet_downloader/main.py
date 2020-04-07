import user_tweet_downloader.tweet_download as td
import user_tweet_downloader.accounts as ac

users = ac.USERS

def main(users):
	print(users)
	for user in users:
		output_file = td.tweet_retrieve(user)
		return output_file


if __name__ == "__main__":
    main(users)


