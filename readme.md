## Delete Crap Reddit Submissions

Deletes subreddit submissions if older than X and score less than X.

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Edit conf.ini with your details
-   Run it `python3 run.py`

### Settings Info

`reddit_user` - Reddit username  
`reddit_pass` - Reddit password  
`reddit_client_id` - Reddit Client ID  
`reddit_client_secret` - Reddit Client Secret  
`reddit_target_subreddits` - List of subreddits to check (comma separated e.g. one,two,three)

`min_days` - Min days old  
`min_score` - Min score  
`test_mode` - Turn on/off (off to delete)
