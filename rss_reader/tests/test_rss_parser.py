import unittest
import requests
from unittest.mock import Mock, patch
from rss_reader.rss_reader_base import RssReader, RssRequestException, RssParseException
from rss_reader.configuration import RssParserConfiguration
from pathlib import Path
from datetime import datetime
import os


def read_text_from_test_file(file_name: str) -> str:
    return Path(os.path.abspath(os.path.join('rss_reader', 'tests', 'test_data', file_name)))\
        .read_text(encoding="utf-8")


def get_test_rss_config() -> "RssParserConfiguration":
    return RssParserConfiguration('https://example.com/rss/', False, False, 2, datetime(2021, 11, 6))


class TestRssParser(unittest.TestCase):

    def test_parse_rss_positive(self):
        expected_rss_content = read_text_from_test_file('example_rss.xml')
        mocked_response = Mock("requests.get")
        mocked_response.status_code = 200
        mocked_response.text = expected_rss_content
        mocked_response.raise_for_status = Mock()
        mocked_logger = Mock()

        with patch('rss_reader.rss_reader_base.requests') as mocked_requests:
            mocked_requests.get.return_value = mocked_response
            rss_reader = RssReader(get_test_rss_config(), Mock(), mocked_logger)
            rss_reader.parse_rss()

        self.assertEqual(rss_reader.response, expected_rss_content)

    def test_parse_rss_negative_unexpected_server_response(self):
        expected_response = requests.Response()
        expected_response.status_code = 500
        expected_response.reason = 'Server is Unavailable'
        expected_response.url = 'https://example.com/rss'
        mocked_logger = Mock()

        with self.assertRaises(RssRequestException) as raised_exception_ctx:
            with patch('rss_reader.rss_reader_base.requests') as mocked_requests:
                mocked_requests.get.return_value = expected_response
                rss_reader = RssReader(get_test_rss_config(), Mock(), mocked_logger)
                rss_reader.parse_rss()
        self.assertEqual(
            'Cannot get RSS from URL provided due to an error: 500 Server Error: '
            'Server is Unavailable for url: https://example.com/rss',
            str(raised_exception_ctx.exception))

    def test_parse_rss_negative_unexpected_feed_format(self):
        server_response = read_text_from_test_file('unexpected_rss_format.html')
        mocked_response = Mock("requests.get")
        mocked_response.status_code = 200
        mocked_response.text = server_response
        mocked_response.raise_for_status = Mock()
        mocked_logger = Mock()

        with self.assertRaises(RssParseException) as raised_exception_ctx:
            with patch('rss_reader.rss_reader_base.requests') as mocked_requests:
                mocked_requests.get.return_value = mocked_response
                rss_reader = RssReader(get_test_rss_config(), Mock(), mocked_logger)
                rss_reader.parse_rss()
        self.assertEqual(
            'Unexpected error during RSS parsing: Unsupported RSS format for url: https://example.com/rss/',
            str(raised_exception_ctx.exception))


if __name__ == '__main__':
    unittest.main()
