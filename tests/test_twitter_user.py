import pytest
import os
import user_tweet_downloader.tweet_download as td
import user_tweet_downloader.jsons_toxlsx as js

ID = "72066060"
USER = "adriapadilla"
RESULT = 16

OUTPUT_FOLDER = "output"
SAVE_PATH="data"



def test_tweet_retrieve(user_id=ID, user_name=USER, result=RESULT):
    jsons = td.tweet_retrieve(user_id, user_name)
    assert len(jsons) == result

def test_convert_all(save_path=SAVE_PATH, user_name=USER, output_folder=OUTPUT_FOLDER):
    xlsx = js.convert_all(save_path, user_name, output_folder)
    assert os.path.exists(xlsx)


