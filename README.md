# User Timeline Downloader

## What is this about?

This script will download the 3.200 most recent tweets of any Twitter public account.

### Twitter API Limitations 

**Particular** ***"GET statuses/user_timeline"*** **method limitations:**

+ 100.000 Requests in a 24h window.
+ You can only collect the 3.200 user's most recent tweets
+ *"GET statuses/user_timeline"* can only return 200 tweets in each request.

**General Twitter Stardard API limits**

App Auth have a 1.500 requests limit in a 15 min window.
We can translate this in:
* 300.000 Tweets downloaded in 15 min window.
* 93 user accounts in a 15 min window. (16 requests are needed to reach the 3.200 most recent tweets for each user).

More information about [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline "Twitter Developer Documentation")

## Installation (Working on it!)

**Option 1: Pip Install**

**Option 2: Hardcode**

## How To Use

