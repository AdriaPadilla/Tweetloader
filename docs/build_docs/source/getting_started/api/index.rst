API
=====


.. code-block:: python

    import user_tweet_downloader.main as td

    usernames = ["adriapadilla", "elpais_espana"]
    user_ids = ["72066060", "121183700"]
    td.retrieve_info(user_ids, usernames)