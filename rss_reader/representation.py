import json
import logging
from rss_reader.entities import RssFeed
from typing import List
from rss_reader.configuration import RssParserConfiguration
from xhtml2pdf import pisa


class RssFormatter:
    def __init__(self, rss_feed: "RssFeed", logger: "logging.Logger"):
        self.rss_feed = rss_feed
        self.logger = logger

    def get_rss_as_text(self) -> str:
        """
        Get RSS as simple text.

        :return: str - simple text representation of RSS feed
        """
        self.logger.info('Starting outputs information about Rss requests to the console')
        result = ''
        result += 'Rss feed title: {title}\nRss feed link: {link}\n' \
                  'Rss feed description: {description}\nRss feed date: {pub_date}\n' \
            .format(title=self.rss_feed.title,
                    link=self.rss_feed.link,
                    description=self.rss_feed.description,
                    pub_date=self.rss_feed.pub_date)

        for item in self.rss_feed.items:
            result += f"\ntitle: {item.title}\nlink: {item.link}\ndate: {item.pub_date}\ndescription: {item.description}\n"
        self.logger.info('Finishing outputs information about Rss requests to the console')
        return result

    def get_rss_as_json(self) -> str:
        """
        Converts RSS into JSON string.

        :return: str - RSS as JSON string
        """
        self.logger.info('Starting process transformation Rss info to Json')
        rss_items = []
        for item in self.rss_feed.items:
            g = {
                'title': item.title,
                'link': item.link,
                'date': item.pub_date.isoformat(),
                'description': item.description
            }
            rss_items.append(g)
        result = {
            'rss_title': self.rss_feed.title,
            'rss_link': self.rss_feed.link,
            'rss_description': self.rss_feed.description,
            'rss_pub_date': self.rss_feed.pub_date.isoformat(),
            'rss_items': rss_items
        }
        json_rss = json.dumps(result, indent=4, ensure_ascii=False)
        self.logger.info('Finishing process transformation Rss info to Json')
        return json_rss

    def get_rss_as_html(self) -> str:
        result = "<html><head><title>RSS reader local files</title></head><body>"
        result += "<h1>{}</h1>".format(self.rss_feed.title)
        for item in self.rss_feed.items:
            result += '<p>Title: {}</p>'.format(item.title)
            result += '<p>Link: {}</p>'.format(item.link)
            result += '<p>Date: {}</p>'.format(item.pub_date)
            result += '<p>Description: {}</p>'.format(item.description)
            result += '<br>'
        result += "</body></html>"
        return result

    def save_rss_as_pdf(self):
        result_file = open(self.rss_feed.title + '.pdf', "w+b")
        pisa.CreatePDF(self.get_rss_as_html(), dest=result_file)
        result_file.close()


def display_rss_feeds(rss_feeds: "List[RssFeed]", config: "RssParserConfiguration", logger: "logging.Logger") -> None:
    for rss_feed in rss_feeds:
        rss_formatter = RssFormatter(rss_feed, logger)
        if config.to_json:
            print(rss_formatter.get_rss_as_json())
        elif config.to_html:
            print(rss_formatter.get_rss_as_html())
        elif config.to_pdf:
            rss_formatter.save_rss_as_pdf()
        else:
            print(rss_formatter.get_rss_as_text())
        print('-' * 50)
