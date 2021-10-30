import logging
import requests
import sys
from bs4 import BeautifulSoup as Bs
from requests.exceptions import RequestException
from rss_reader.utils.common_utils import extract_text, is_valid_rss, parse_arguments, parse_date_from_rss
from rss_reader.configuration import RssParserConfiguration
from rss_reader.entities import RssFeed, RssItem
from rss_reader.storage import StorageLayer, NoContentFound
from rss_reader.representation import display_rss_feeds


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


class RssReader:
    """
    Main class for parsing RSS feed
    """

    def __init__(self, config: "RssParserConfiguration", storage: "StorageLayer", logger: "logging.Logger"):
        self.config = config
        self.storage = storage
        self.logger = logger
        self.response = None
        self.rss_feed = None

    def _get_rss_feed(self) -> None:
        """
        Retrieves RSS feed from the remote server using the URL.

        :raises RssRequestException if there was an exception during HTTP request
        """
        try:
            self.logger.info('Starting the process of getting the request object')
            r = requests.get(self.config.source_url)
            r.raise_for_status()
            self.response = r.text
            self.logger.info('Successfully accepted the response object')
        except RequestException as e:
            self.logger.exception(f"Cannot get RSS from URL provided due to an error: ", exc_info=e)
            raise RssRequestException(f"Cannot get RSS from URL provided due to an error: {e}")

    def parse_rss(self) -> "RssFeed":
        """
        Retrieves RSS feed from URL and parses it.

        :raises RssParseException if there was an exception during rss parsing
        """
        self._get_rss_feed()
        try:
            self.logger.info('Starting RSS parsing')
            soup = Bs(self.response, features='xml')
            if not is_valid_rss(soup):
                raise RssParseException(f'Unsupported RSS format for url: {self.config.source_url}')
            items = soup.find_all('item')
        except Exception as e:
            self.logger.error('Unexpected error during RSS parsing: ', exc_info=e)
            raise RssParseException(f"Unexpected error during RSS parsing: {e}")
        channel = soup.find('channel')
        self.rss_feed = RssFeed(
            self.config.source_url,
            extract_text(channel.title),
            extract_text(channel.link),
            parse_date_from_rss(extract_text(channel.pubDate)),
            extract_text(channel.description))
        rss_limit = self.config.limit
        number_elements_to_process = len(items) if rss_limit is None else abs(rss_limit)
        for index in range(number_elements_to_process):
            item = items[index]
            title = extract_text(item.title)
            link = extract_text(item.link)
            date = extract_text(item.pubDate)
            description = extract_text(item.description)
            self.rss_feed.add_item(RssItem(title, link, parse_date_from_rss(date), description))
        self.logger.info('Successfully parsed RSS feed')
        self.logger.info('Saving RSS feed to local storage')
        self.storage.save_rss_feed(self.rss_feed)
        self.logger.info('Successfully saved RSS feed to local storage')
        return self.rss_feed


def main():
    logging.basicConfig(handlers=[logging.StreamHandler()])
    logger = logging.getLogger('rss_reader')
    config = parse_arguments(sys.argv[1:], logger)
    logger.setLevel(logging.DEBUG if config.verbose else logging.WARNING)

    storage_layer = StorageLayer()

    rss_feeds = []
    if config.date:
        try:
            if config.source_url:
                rss_feeds.append(storage_layer.read_rss_feed(config.date, config.source_url, config.limit))
            else:
                rss_feeds.extend(storage_layer.read_rss_feeds(config.date, config.limit))
        except NoContentFound as e:
            print(e)
            sys.exit()
    else:
        rss_reader = RssReader(config, storage_layer, logger)
        rss_feeds.append(rss_reader.parse_rss())

    display_rss_feeds(rss_feeds, config, logger)


if __name__ == '__main__':
    main()
