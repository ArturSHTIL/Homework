from datetime import datetime


class RssFeed:
    """
    Represents RSS feed
    """
    def __init__(self, source_url: str, title: str, link: str, pub_date: datetime, description: str):
        self.source_url = source_url
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date
        self.items = []

    def add_item(self, item: "RssItem"):
        self.items.append(item)

    def __eq__(self, other):
        if isinstance(other, RssFeed):
            return self.source_url == other.source_url \
                   and self.title == other.title \
                   and self.link == other.link \
                   and self.description == other.description \
                   and self.pub_date == other.pub_date \
                   and self.items == other.items
        return False


class RssItem:
    """
    Represents an article in RSS feed
    """
    def __init__(self, title: str, link: str, pub_date: datetime, description: str = None):
        self.title = title
        self.pub_date = pub_date
        self.link = link
        self.description = description

    def __eq__(self, other):
        if isinstance(other, RssItem):
            return self.title == other.title \
                   and self.pub_date == other.pub_date \
                   and self.link == other.link \
                   and self.description == other.description
        return False
