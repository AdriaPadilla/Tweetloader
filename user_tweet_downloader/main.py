import user_tweet_downloader.tweet_download as td
import user_tweet_downloader.accounts as ac

user_ids = ac.IDS
usernames = ac.USERS

if __name__ == "__main__":
    for userid, username in zip(user_ids, usernames):
        td.tweet_retrieve(userid, username)


