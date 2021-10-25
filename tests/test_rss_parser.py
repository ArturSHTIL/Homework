import unittest
import requests
from unittest.mock import Mock, patch
from rss_reader import RssReader, RssRequestException, RssParseException
from pathlib import Path
import os


def read_text_from_test_file(file_name: str) -> str:
    return Path(os.path.abspath(os.path.join('tests', 'test_data', file_name))).read_text(encoding="utf-8")


class TestRssParser(unittest.TestCase):

    def test_parse_rss_positive(self):
        expected_rss_content = read_text_from_test_file('example_rss.xml')
        mocked_response = Mock("requests.get")
        mocked_response.status_code = 200
        mocked_response.text = expected_rss_content
        mocked_response.raise_for_status = Mock()
        mocked_logger = Mock()

        with patch('rss_reader.requests') as mocked_requests:
            mocked_requests.get.return_value = mocked_response
            rss_reader = RssReader('https://example.com/rss/', mocked_logger, 5)
            rss_reader.parse_rss()

        self.assertEqual(rss_reader.response, expected_rss_content)

    def test_parse_rss_negative_unexpected_server_response(self):
        expected_response = requests.Response()
        expected_response.status_code = 500
        expected_response.reason = 'Server is Unavailable'
        expected_response.url = 'https://example.com/rss'
        mocked_logger = Mock()

        with self.assertRaises(RssRequestException) as raised_exception_ctx:
            with patch('rss_reader.requests') as mocked_requests:
                mocked_requests.get.return_value = expected_response
                rss_reader = RssReader('https://example.com/rss/', mocked_logger, 5)
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
            with patch('rss_reader.requests') as mocked_requests:
                mocked_requests.get.return_value = mocked_response
                rss_reader = RssReader('https://example.com/rss/', mocked_logger, 5)
                rss_reader.parse_rss()
        self.assertEqual(
            'Unexpected error during RSS parsing: Unsupported RSS format for url: https://example.com/rss/',
            str(raised_exception_ctx.exception))

    def test_get_rss_as_text_positive(self):
        expected_rss_content = read_text_from_test_file('example_rss.xml')
        mocked_response = Mock("requests.get")
        mocked_response.status_code = 200
        mocked_response.text = expected_rss_content
        mocked_response.raise_for_status = Mock()
        mocked_logger = Mock()

        with patch('rss_reader.requests') as mocked_requests:
            mocked_requests.get.return_value = mocked_response
            rss_reader = RssReader('https://example.com/rss/', mocked_logger, 2)
            rss_reader.parse_rss()

            actual = rss_reader.get_rss_as_text()

        self.assertEqual('''Rss feed title: Люди Onlíner
Rss feed link: https://people.onliner.by/
Rss feed description: Люди Onlíner
Rss feed date: Sun, 17 Oct 2021 11:03:45 +0300

title: 14-летняя белоруска победила на престижном международном фестивале в Италии
link: https://people.onliner.by/2021/10/17/beloruska-pobedila-na-festivale-v-italii
date: Sun, 17 Oct 2021 11:03:45 +0300
description: 14-летняя солистка продюсерского центра «Спамаш» Ксения Галецкая выиграла престижный детский вокальный конкурс sanremoJunior, сообщили в инстаграм-аккаунте центра. Ксения исполнила хит Who’s Loving You.Читать далее…

title: Матулям прысвячаецца. Спецвыпуск беларускіх шпаргалак
link: https://people.onliner.by/2021/10/17/specvypusk-shpargalak-3
date: Sun, 17 Oct 2021 10:00:08 +0300
description: 14 кастрычніка многія беларусы адзначалі Дзень маці, таму сённяшні выпуск нашых традыцыйных шпаргалак прысвечаны мамам. Мы вырашылі паглядзець, як тэма адносін да мацеры адлюстравана ў прыказках, прымаўках ды параўнаннях — тым, што робіць наша маўленне больш багатым, яскравым і адметным. Запамінайце ўстойлівыя трапныя выразы і карыстайцеся імі пры нагодзе.Читать далее…\n''', actual)

    def test_get_rss_as_json_positive(self):
        expected_rss_content = read_text_from_test_file('example_rss.xml')
        mocked_response = Mock("requests.get")
        mocked_response.status_code = 200
        mocked_response.text = expected_rss_content
        mocked_response.raise_for_status = Mock()
        mocked_logger = Mock()

        with patch('rss_reader.requests') as mocked_requests:
            mocked_requests.get.return_value = mocked_response
            rss_reader = RssReader('https://example.com/rss/', mocked_logger, 2)
            rss_reader.parse_rss()
            actual = rss_reader.get_rss_as_json()

        self.assertEqual('''{
    "rss_title": "Люди Onlíner",
    "rss_link": "https://people.onliner.by/",
    "rss_description": "Люди Onlíner",
    "rss_pub_date": "Sun, 17 Oct 2021 11:03:45 +0300",
    "rss_items": [
        {
            "title": "14-летняя белоруска победила на престижном международном фестивале в Италии",
            "link": "https://people.onliner.by/2021/10/17/beloruska-pobedila-na-festivale-v-italii",
            "date": "Sun, 17 Oct 2021 11:03:45 +0300",
            "description": "14-летняя солистка продюсерского центра «Спамаш» Ксения Галецкая выиграла престижный детский вокальный конкурс sanremoJunior, сообщили в инстаграм-аккаунте центра. Ксения исполнила хит Who’s Loving You.Читать далее…"
        },
        {
            "title": "Матулям прысвячаецца. Спецвыпуск беларускіх шпаргалак",
            "link": "https://people.onliner.by/2021/10/17/specvypusk-shpargalak-3",
            "date": "Sun, 17 Oct 2021 10:00:08 +0300",
            "description": "14 кастрычніка многія беларусы адзначалі Дзень маці, таму сённяшні выпуск нашых традыцыйных шпаргалак прысвечаны мамам. Мы вырашылі паглядзець, як тэма адносін да мацеры адлюстравана ў прыказках, прымаўках ды параўнаннях — тым, што робіць наша маўленне больш багатым, яскравым і адметным. Запамінайце ўстойлівыя трапныя выразы і карыстайцеся імі пры нагодзе.Читать далее…"
        }
    ]
}''', actual)


if __name__ == '__main__':
    unittest.main()
