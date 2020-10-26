# Tweetloader

Version 2
Citation APA Style: Padilla Molina, Adrian (2020). Tweetloader (Version 2) [Software]. Avaliable from: https://github.com/AdriaPadilla/Tweetloader

#### Critical Dependencies
```bash
- pip install pandas
- pip install openpyxl
- pip install TwitterAPI
```
#### Also needed Dependencies
```bash
json, glob, os, time, argparse, textwrap
```

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

**Step 1: Download Tweetloader to your computer**

```Terminal
...$: git clone https://github.com/AdriaPadilla/Tweetloader.git
````

**If you don't have "git" installed. Download zip package, then unzip the package in a desired folder**

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

### 3.2. Usage ###

This is a terminal execution software. You have to use arguments to start the process. Read the following lines.

**Step 1: Open your windows/mac/linux terminal**

1. Go to the installation folder
2. Ho to make a query

#### Commands ####

##### Mandatory commands #####
```bash
-- u username (or a list)
```
F.e: This command will download the latest 3200 tweets from my personal account
```bash
python main.py -u adriapadilla
```
You can also input a list of users, one after the other, without using commas. Only separated by a space:
```bash
python main.py -u adriapadilla anotheruser anotheruser etc etc
```

##### Non-mandatory commands #####
```bash
-c [To create a single DataSet with all defined users. Disabled by default]
-j [To Preserve original JSON files from API Response. Deleted by default]
```

F.e: this command will:
- download the latest 3200 tweets from the desired accounts.
- create a single dataset with all tweets.
- preserve in your computer all Twitter API responses in JSON format.
```bash
python main.py --u uername1 username2 username3 -c -j
```

### 3.3. The Output ###

The application will create a new folder named "output", and a new subfolder for each user you want to capture. In this subfolder you'll find:

+ All Twitter API's responde in .json format.
+ One .xlsx format file with data.
+ If you use -c argument, you'll also have a single dataset with all accounts data.
