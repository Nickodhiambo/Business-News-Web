#Standard Library
import logging

#Django
from django.conf import settings
from django.core.management.base import BaseCommand

#Third party
import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

# My app
from news_content.models import Content

logger = logging.getLogger(__name__)


def save_content_to_db(feed):
    """Saves rss feed data to database"""
    site_title = feed.channel.title

    for item in feed.entries:
        if not Content.objects.filter(guid=item.guid).exists():
            content = Content(
                    title=item.title,
                    description=item.description,
                    link=item.link,
                    pub_date = parser.parse(item.published),
                    guid=item.guid,
                    site_name = site_title,
                    )
            content.save()

def fetch_business_daily():
    feed = feedparser.parse("https://www.businessdailyafrica.com/service/rss/bd/1939132/feed.rss")
    save_content_to_db(feed)

def fetch_african_business():
    feed = feedparser.parse("https://african.business/feed")
    save_content_to_db(feed)

def fetch_financial_fortune():
    feed = feedparser.parse("https://www.financialfortunemedia.com/feed/")
    save_content_to_db(feed)


class Command(BaseCommand):
    """A custom command class"""
    def handle(self, *args, **kwargs):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
                fetch_business_daily,
                trigger="interval",
                minutes=2,
                id="Business Daily",
                max_instances=1,
                replace_existing=True,
                )
        logger.info("Added job: The Business Daily.")

        scheduler.add_job(
                fetch_african_business,
                trigger="interval",
                minutes=2,
                id="African Business",
                max_instances=1,
                replace_existing=True,
                )
        logger.info("Added job: The African Business.")
        
        scheduler.add_job(
                fetch_financial_fortune,
                trigger="interval",
                minutes=2,
                id="Financial Fortune",
                max_instances=1,
                replace_existing=True,
                )
        logger.info("Added job: The Financial Fortune.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
