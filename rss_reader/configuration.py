from datetime import datetime


class RssParserConfiguration:
    def __init__(self, source_url: str, to_json: bool, to_html: bool, to_pdf: bool, verbose: bool, limit: int, date: datetime):
        self.source_url = source_url
        self.to_json = to_json
        self.to_html = to_html
        self.to_pdf = to_pdf
        self.verbose = verbose
        self.limit = limit
        self.date = date
