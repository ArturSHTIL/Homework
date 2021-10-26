import argparse
import logging
import bs4
import requests
import sys
import json
from bs4 import BeautifulSoup as Bs
from datetime import datetime
from requests.exceptions import RequestException


class RssParseException(Exception):
    """
    Raised if there was an error during RSS parsing
    """
    pass


class RssRequestException(Exception):
    """
    Raised if there was an error during HTTP request for RSS feed
    """
    pass


def parse_arguments(args, logger_):
    """
    Parses user input from command line.

    :param args: Optional arguments: 'source', Positional arguments: '--version', "--json", "--verbose", "--limit"
    :param logger_: logging for get info
    :return: tuple(args)
    """

    logger_.info('Starting the process getting argparse arguments')
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    parser.add_argument("source", help='RSS URL', type=str)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.2')
    parser.add_argument("--json", help='Print result as JSON in stdout', action="store_true")
    parser.add_argument("--verbose", help='Outputs verbose status messages', action="store_true")
    parser.add_argument("--limit", help=f'Limit news topics if this parameter provided', type=int, default=None)
    args = parser.parse_args(args)
    logger_.info('Finishing the process getting argparse arguments')
    return args.source, args.json, args.verbose, args.limit


def extract_text(tag: bs4.Tag) -> str:
    """
    Extract text from a Tag depending on its conte and removing whitespaces.

    :param tag: bs4.Tag
    :return: str - tag content as a string
    """
    if tag is None:
        return ''
    element_text = tag.text.strip()
    if '/>' in element_text or '<p>' in element_text:
        html_parser = bs4.BeautifulSoup(tag.text, 'html.parser')
        return html_parser.get_text().strip()
    return element_text


def is_valid_rss(parser: bs4.BeautifulSoup) -> bool:
    """
    Check if markup is a valid RSS feed.

    :param parser: bs4.BeautifulSoup
    :return: bool
    """
    rss_tag = parser.find('rss')
    return rss_tag is not None


class RssReader:
    """
    Main class for parsing RSS feed
    """

    def __init__(self, url: str, logger_: "logging.Logger", limit: int):
        self.url = url
        self.logger = logger_
        self.limit = limit
        self.response = None
        self.rss_feed = None

    def _get_rss_feed(self) -> None:
        """
        Retrieves RSS feed from the remote server using the URL.

        :raises RssRequestException if there was an exception during HTTP request
        """
        try:
            self.logger.info('Starting the process of getting the request object')
            r = requests.get(self.url)
            r.raise_for_status()
            self.response = r.text
            self.logger.info('Successfully accepted the response object')
        except RequestException as e:
            self.logger.exception(f"Cannot get RSS from URL provided due to an error: ", exc_info=e)
            raise RssRequestException(f"Cannot get RSS from URL provided due to an error: {e}")

    def parse_rss(self) -> None:
        """
        Retrieves RSS feed from URL and parses it.

        :raises RssParseException if there was an exception during rss parsing
        """
        self._get_rss_feed()
        try:
            self.logger.info('Starting RSS parsing')
            soup = Bs(self.response, features='xml')
            if not is_valid_rss(soup):
                raise RssParseException(f'Unsupported RSS format for url: {self.url}')
            items = soup.find_all('item')
        except Exception as e:
            self.logger.error('Unexpected error during RSS parsing: ', exc_info=e)
            raise RssParseException(f"Unexpected error during RSS parsing: {e}")
        channel = soup.find('channel')
        self.rss_feed = RssFeed(
            extract_text(channel.title),
            extract_text(channel.link),
            extract_text(channel.pubDate),
            extract_text(channel.description))

        number_elements_to_process = len(items) if self.limit is None else abs(self.limit)
        for index in range(number_elements_to_process):
            item = items[index]
            title = extract_text(item.title)
            link = extract_text(item.link)
            date = extract_text(item.pubDate)
            description = extract_text(item.description)
            self.rss_feed.add_item(RssItem(title, link, date, description))
        self.logger.info('Successfully parsed RSS feed')

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
            result += f"\ntitle: {item.title}\nlink: {item.link}\ndate: {item.date}\ndescription: {item.description}\n"
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
                'date': item.date,
                'description': item.description
            }
            rss_items.append(g)
        result = {
            'rss_title': self.rss_feed.title,
            'rss_link': self.rss_feed.link,
            'rss_description': self.rss_feed.description,
            'rss_pub_date': self.rss_feed.pub_date,
            'rss_items': rss_items
        }
        json_rss = json.dumps(result, indent=4, ensure_ascii=False)
        self.logger.info('Finishing process transformation Rss info to Json')
        return json_rss


class RssFeed:
    """
    Represents RSS feed
    """

    def __init__(self, title: str, link: str, pub_date: datetime, description: str):
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date
        self.items = []

    def add_item(self, item: "RssItem"):
        self.items.append(item)


class RssItem:
    """
    Represents an article in RSS feed
    """

    def __init__(self, title: str, link: str, date: str, description: str = None):
        self.title = title
        self.date = date
        self.link = link
        self.description = description


def main():
    logging.basicConfig(handlers=[logging.StreamHandler()])
    logger = logging.getLogger('rss_reader')
    source_url_, json_, verbose_, limit_ = parse_arguments(sys.argv[1:], logger)
    logger.setLevel(logging.DEBUG if verbose_ else logging.WARNING)

    rss_news = RssReader(source_url_, logger, limit_)
    rss_news.parse_rss()
    if json_:
        print(rss_news.get_rss_as_json())
    else:
        print(rss_news.get_rss_as_text())


if __name__ == '__main__':
    main()
