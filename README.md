# User Timeline Downloader

## What is this about?

This script will download the 3.200 most recent tweets of any Twitter public account.

### Limitations 

**Particular** ***"GET statuses/user_timeline"*** **method limitations:**

+ 100.000 Requests in a 24h window.
+ You can only collect the 3.200 user's most recent tweets

**General Twitter Stardard API limits**

*"GET statuses/user_timeline"* method have a 1.500 requests Limit (Using  app auth) in a 15 min window. 
We can translate this in:
* 300.000 Tweets in 15 min window.
* 93 user accounts in a 15 min window. (16 requests are needed to reach the 3.200 most recent tweets for each user).

More information about [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline "Twitter Developer Documentation")
