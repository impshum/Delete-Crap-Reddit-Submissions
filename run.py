import praw
import configparser
import datetime


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddits = config['REDDIT']['reddit_target_subreddits'].split(',')
min_days = int(config['SETTINGS']['min_days'])
min_score = int(config['SETTINGS']['min_score'])
test_mode = config['SETTINGS'].getboolean('test_mode')

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Delete Crap Reddit Submissions (by u/impshum)'
)


def main():
    if test_mode:
        print('TEST MODE')

    utc_now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).timestamp()

    for reddit_target_subreddit in reddit_target_subreddits:
        for submission in reddit.subreddit(reddit_target_subreddit).new(limit=None):
            if submission.created_utc < utc_now - ((3600 * 24) * min_days) and submission.score < min_score:
                if not test_mode:
                    submission.mod.remove()
                print(f'REMOVED - {submission.title}')


if __name__ == '__main__':
    main()
