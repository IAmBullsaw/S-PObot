import time
import sys
from prawcore import ServerError
import praw


def get_sweddit():
    """
    Creates the Reddit instance
    :return: the subreddit /r/sweden
    """
    # FIXME: Seems like this does not properly authenticate/log in.
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
    successful = False
    while retries:
        retries -= 1
        try:
            submissions = next(submissions)
            successful = True
            break
        except ServerError as e:
            print('Received', e.response, '... retry in %d seconds:' % wait, retries, file=sys.stderr)
            time.sleep(wait)
    return submissions if successful else None


def main():
    sweddit = get_sweddit()

    submissions = get_submissions(sweddit)
    if not submissions:
        print("[ERROR] Didn't get any submissions ... ", file=sys.stderr)
        exit(1)

    for submission in submissions:
        print(submission.title)


if __name__ == '__main__':
    main()
