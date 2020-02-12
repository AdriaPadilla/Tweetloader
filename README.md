# User Timeline Downloader

## 1. What is this about?

This script will download the 3.200 most recent tweets of any Twitter public account.

## 2. Twitter API Limitations 

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

## 3. Installation

**Option 1: Pip install**

```Terminal
...$: pip install user_tweet_downloader
````

**Option 2: Hardcode**

Step 1: Clone this repository in your pc

```bash
...$: git clone https://github.com/AdriaPadilla/user_tweet_downloader.git 
```

Step 2: Access the main folder
```
...$: cd user_tweet_downloader
```

Step 3: Execute install

```
.../user_tweet_downloader/$: python3 setup.py install

```

### 3.1. Configuration ###

To use this applications, you'll need Twitter API credentials: 


1. Go to: https://developer.twitter.com/ 
2. Create a new account.
3. Go: https://developer.twitter.com/en/apps
4. Create a click "create an app".
5. Follow the instructions.

For each "app" you create, you'll get 4 keys: Consumer Key, Consumer Secret Key, Access token Key, Access token secret Key. 

Open "constants.py" and place your credentials between " ":

```bash
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""
```

### 3.2. Command instructions ###

user_tweet_downloader works with "argparse". To start a capture you'll need: the visible "username" and the "user id". 

F.e.: my twitter visible username is "adriapadilla" and my user id is "tt1520211". You can find the user's id using this tool: http://gettwitterid.com/


In your terminal:
```bash
...$: python3 -m user_tweet_downloader.main --name userame --id user_id

```
f.e.:
```bash
...$: python3 -m user_tweet_downloader.main --name adriapadilla --id 72066060
```

This will capture the latest 3200 tweets from my personal account

The same with a list of users:
```bash
...$: python3 -m user_tweet_downloader.main --name adriapadilla username_2  etc --id 72066060 user_id_2 etc
```

***important: You have to follow the same order in user_names and users_id. The second User_ID must match with the second User_name.***



### 3.3. Hardcode use (Method for big queries) ###



If you have a big bunch of accounts to scrape, command line can be very annoying. Please, use this method:

Steps:
1. Go to the installation folder
2. find users_lits.py
3. Follow the instructions in the head of the file

In **users_list.py** you can place a large list of user_names and user_id's to make big queries. 

To execute the querie, just run main.py:

```bash
.../your_path_to/user_tweet_downloader/$: pithon3 main.py
```

**Note: Follow the same order placing user_IDS and user_Names... Must be in the same order**


### 3.3. The Output ###

The application will create a new folder named "output", and a new subfolder for each user you want to capture. In this subfolder you'll find:

+ All Twitter API's responde in .json format
+ One .xlsx format file with data
