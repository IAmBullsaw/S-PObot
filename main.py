import time
import praw
from prawcore import ServerError


def get_sweddit():
    """
    Creates the Reddit instance
    :return: the subreddit /r/sweden
    """
    reddit = praw.Reddit(site_name='S-PO')
    sub = reddit.subreddit('sweden')
    return sub


def get_submissions(sweddit, retries=5, wait=10, limit=10):
    """
    Will get hot submissions, retries on ServerError
    :param sweddit: subreddit
    :param retries: how many retries
    :param wait: how long to wait between retries
    :param limit: the amount of posts in each request
    :return: the amount of submissions from sweddits hot up to limit
    """
    submissions = sweddit.hot(limit=limit)
    while retries:
        retries -= 1
        try:
            submissions = next(submissions)
            break
        except ServerError as e:
            print(e.__str__(), 'will retry in %d seconds:' % limit, retries)
            time.sleep(wait)
    return submissions


def main():
    sweddit = get_sweddit()

    submissions = get_submissions(sweddit)
    for submission in submissions:
        print(submission.title)


if __name__ == '__main__':
    main()
