from datetime import datetime


class RssParserConfiguration:
    def __init__(self, source_url: str, to_json: bool, verbose: bool, limit: int, date: datetime):
        self.source_url = source_url
        self.to_json = to_json
        self.verbose = verbose
        self.limit = limit
        self.date = date
