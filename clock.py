from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
import todays_kurunthogai
from local_config import *

tweet_scheduler = BlockingScheduler()


@tweet_scheduler.scheduled_job('cron', id='kurunthogai_tweet_scheduler',
                               day_of_week=TWEET_SCHEDULE_DAY,
                               hour=int(TWEET_SCHEDULE_HOUR), minute=int(TWEET_SCHEDULE_MINUTE))
def scheduled_tweeter_job():
    print("Beginning the scheduled job")
    todays_kurunthogai.tweet_todays_kurunthogai()
    print("Executed the scheduled job")


# Schedule job_function to be called every two hours
# tweet_scheduler.add_job(scheduled_tweeter_job, 'interval', seconds=10)

tweet_scheduler.start()
