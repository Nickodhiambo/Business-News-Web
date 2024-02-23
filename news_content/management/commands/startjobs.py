from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser
from news_content.models import Content


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
        fetch_business_daily()
        fetch_african_business()
        fetch_financial_fortune()
