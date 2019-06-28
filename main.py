import praw

# Create the Reddit instance and log in
REDDIT_USERNAME = 'hej'
REDDIT_PASS = 'balle'
reddit = praw.Reddit('bot')

reddit.login(REDDIT_USERNAME, REDDIT_PASS)
