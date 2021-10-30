from datetime import datetime, timezone
from dateutil import parser
import argparse
import bs4
from rss_reader.configuration import RssParserConfiguration


def _handle_date(date: str) -> datetime:
    try:
        dt = datetime.strptime(date, "%Y%m%d")
        dt = datetime(dt.year, dt.month, dt.day, tzinfo=timezone.utc)
        return dt
    except ValueError:
        raise argparse.ArgumentTypeError("not a valid date: {0!r}".format(date))


def parse_date_from_rss(date_as_str: str) -> datetime:
    dt = parser.parse(date_as_str)
    return datetime.fromtimestamp(dt.timestamp(), tz=timezone.utc)


def convert_datetime_to_timestamp(datetime_obj: "datetime"):
    return int(datetime_obj.timestamp())


def convert_timestamp_to_datetime(ts: int):
    return datetime.fromtimestamp(ts)


def parse_arguments(args, logger_):
    """
    Parses user input from command line.

    :param args: Optional arguments: 'source', Positional arguments: '--version', "--json", "--verbose", "--limit"
    :param logger_: logging for get info
    :return: tuple(args)
    """
    if not args:
        raise argparse.ArgumentTypeError('At least one of the following parameters should be provided:'
                                         ' [source] or [--date DATE]')
    logger_.info('Starting the process getting argparse arguments')
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    parser.add_argument("source", help='RSS URL', type=str, nargs="?", default=None)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.2')
    parser.add_argument("--json", help='Print result as JSON in stdout', action="store_true")
    parser.add_argument("--to-html", help='Print result as HTML in stdout', action="store_true")
    parser.add_argument("--to-pdf", help='Save RSS as pdf in current directory', action="store_true")
    parser.add_argument("--verbose", help='Outputs verbose status messages', action="store_true")
    parser.add_argument("--limit", help='Limit news topics if this parameter provided', type=int, default=None)
    parser.add_argument("--date", help='', type=_handle_date, default=None)
    args = parser.parse_args(args)
    logger_.info('Finishing the process getting argparse arguments')
    return RssParserConfiguration(args.source, args.json, args.to_html, args.to_pdf, args.verbose, args.limit, args.date)


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
