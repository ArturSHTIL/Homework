import datetime
import sqlite3
from rss_reader.entities import RssFeed, RssItem
from rss_reader.utils.common_utils import convert_datetime_to_timestamp, convert_timestamp_to_datetime
from typing import List


CREATE_RSS_FEED_TABLE_QUERY = """
        CREATE TABLE if not exists rss_feed (
                source_url TEXT PRIMARY KEY,
                title TEXT,
                link TEXT,
                date INTEGER,
                description TEXT)"""
CREATE_RSS_ITEM_TABLE_QUERY = """
        CREATE TABLE if not exists rss_item (
                source_url TEXT,
                title TEXT,
                link TEXT,
                date INTEGER,
                description TEXT,
                UNIQUE(source_url, link, date),
                FOREIGN KEY(source_url) REFERENCES rss_feed(source_url))"""
INSERT_INTO_RSS_FEED_TABLE = """INSERT OR IGNORE INTO rss_feed VALUES(?, ?, ?, ?, ?)"""
INSERT_INTO_RSS_ITEM_TABLE = """INSERT OR IGNORE INTO rss_item VALUES(?, ?, ?, ?, ?)"""
SELECT_ALL_FROM_RSS_FEED_TABLE = "SELECT * FROM rss_feed"
SELECT_ALL_FROM_RSS_FEED_TABLE_BY_SOURCE_URL = "SELECT * FROM rss_feed WHERE source_url = ?"
SELECT_ALL_FROM_RSS_ITEM_TABLE_BY_DATE_AND_SOURCE_URL = """
        SELECT * FROM rss_item WHERE date(date, 'unixepoch') = date(?, 'unixepoch') AND source_url = ?"""
SELECT_ALL_FROM_RSS_ITEM_TABLE_BY_LINK = """SELECT * FROM rss_item WHERE link = ?"""


class NoContentFound(Exception):
    pass


class NoContentForSourceFound(NoContentFound):
    pass


class NoRssArticlesForSourceAndDateFound(NoContentFound):
    pass


class StorageLayer:
    def __init__(self):
        self.conn = sqlite3.connect('local_storage.db', isolation_level=None)
        self._create_tables()

    def save_rss_feed(self, rss_feed: "RssFeed") -> None:
        cursor = self.conn.cursor()
        rss_feed_values = (rss_feed.source_url,
                           rss_feed.title,
                           rss_feed.link,
                           convert_datetime_to_timestamp(rss_feed.pub_date),
                           rss_feed.description)
        cursor.execute(INSERT_INTO_RSS_FEED_TABLE, rss_feed_values)
        for rss_item in rss_feed.items:
            rss_item_value = (rss_feed.source_url,
                              rss_item.title,
                              rss_item.link,
                              convert_datetime_to_timestamp(rss_item.pub_date),
                              rss_item.description)
            cursor.execute(INSERT_INTO_RSS_ITEM_TABLE, rss_item_value)
        cursor.close()

    def read_rss_feed(self, date: datetime, source_url: str, limit: int = None) -> "RssFeed":
        cursor = self.conn.cursor()
        rss_feed_row = cursor.execute(SELECT_ALL_FROM_RSS_FEED_TABLE_BY_SOURCE_URL, (source_url,)).fetchone()
        if rss_feed_row is None:
            raise NoContentForSourceFound('Nothing is stored locally for source "{}"'.format(source_url))
        rss_feed = StorageLayer._convert_row_to_rss_feed(rss_feed_row)
        if limit:
            rss_item_rows = cursor.execute(
                SELECT_ALL_FROM_RSS_ITEM_TABLE_BY_DATE_AND_SOURCE_URL, (convert_datetime_to_timestamp(date), source_url)
            ).fetchmany(limit)
        else:
            rss_item_rows = cursor.execute(
                SELECT_ALL_FROM_RSS_ITEM_TABLE_BY_DATE_AND_SOURCE_URL, (convert_datetime_to_timestamp(date), source_url)
            ).fetchall()
        if len(rss_item_rows) == 0:
            raise NoRssArticlesForSourceAndDateFound('Nothing is stored locally for source "{}" and date "{}"'.format(source_url, date.date()))
        StorageLayer._convert_to_rss_items_and_update_rss_feed(rss_item_rows, rss_feed)
        cursor.close()
        return rss_feed

    def read_rss_feeds(self, date: datetime, limit: int = None) -> "List[RssFeed]":
        rss_feeds = []
        cursor = self.conn.cursor()
        rss_feed_rows = cursor.execute(SELECT_ALL_FROM_RSS_FEED_TABLE).fetchall()
        if len(rss_feed_rows) == 0:
            raise NoContentFound('Local storage is empty')
        for feed_row in rss_feed_rows:
            rss_feed = StorageLayer._convert_row_to_rss_feed(feed_row)
            try:
                rss_feeds.append(self.read_rss_feed(date, rss_feed.source_url, limit))
            except NoRssArticlesForSourceAndDateFound:
                continue
        cursor.close()
        return rss_feeds

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(CREATE_RSS_FEED_TABLE_QUERY)
        cursor.execute(CREATE_RSS_ITEM_TABLE_QUERY)

    @staticmethod
    def _convert_row_to_rss_feed(row: tuple) -> "RssFeed":
        return RssFeed(row[0], row[1], row[2], convert_timestamp_to_datetime(row[3]), row[4])

    @staticmethod
    def _convert_to_rss_items_and_update_rss_feed(rows: List[tuple], rss_feed: "RssFeed") -> None:
        for row in rows:
            rss_feed.add_item(
                RssItem(row[1], row[2], convert_timestamp_to_datetime(row[3]), row[4])
            )
