import unittest
import rss_reader.utils.common_utils as common_utils
from unittest.mock import Mock
from datetime import datetime, timezone
from argparse import ArgumentTypeError


class TestArgumentParsing(unittest.TestCase):

    def test_args_parse_defaults(self):
        with self.assertRaises(ArgumentTypeError) as context:
            common_utils.parse_arguments([], Mock())
            self.assertEqual('At least one of the following parameters should be provided: [source] or [--date DATE]',
                             str(context.exception))


    def test_only_required_args_parse_positive(self):
        actual_rss_config = common_utils.parse_arguments(['https://example.com/rss/'], Mock())
        self.assertEqual('https://example.com/rss/', actual_rss_config.source_url)
        self.assertEqual(False, actual_rss_config.to_json)
        self.assertEqual(False, actual_rss_config.verbose)
        self.assertEqual(None, actual_rss_config.limit)

    def test_limit_args_parse_positive(self):
        actual_rss_config = common_utils.parse_arguments(['https://example.com/rss/', '--limit=2'], Mock())
        self.assertEqual('https://example.com/rss/', actual_rss_config.source_url)
        self.assertEqual(False, actual_rss_config.to_json)
        self.assertEqual(False, actual_rss_config.verbose)
        self.assertEqual(2, actual_rss_config.limit)

    def test_json_arg_parse_positive(self):
        actual_rss_config = common_utils.parse_arguments(['https://example.com/rss/', '--json'], Mock())
        self.assertEqual('https://example.com/rss/', actual_rss_config.source_url)
        self.assertEqual(True, actual_rss_config.to_json)
        self.assertEqual(False, actual_rss_config.verbose)
        self.assertEqual(None, actual_rss_config.limit)

    def test_verbose_arg_parse_positive(self):
        actual_rss_config = common_utils.parse_arguments(['https://example.com/rss/', '--verbose'], Mock())
        self.assertEqual('https://example.com/rss/', actual_rss_config.source_url)
        self.assertEqual(False, actual_rss_config.to_json)
        self.assertEqual(True, actual_rss_config.verbose)
        self.assertEqual(None, actual_rss_config.limit)

    def test_parse_date_positive(self):
        actual = common_utils._handle_date('20211106')
        self.assertEqual(datetime(2021, 11, 6, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc), actual)

    def test_parse_date_negative(self):
        with self.assertRaises(ArgumentTypeError) as context:
            common_utils._handle_date('2021-11-06')
            self.assertEqual('not a valid date: 2021-11-06', str(context.exception))

    def test_date_arg_parse_positive(self):
        actual_rss_config = common_utils.parse_arguments(['https://example.com/rss/', '--date=20211106'], Mock())
        self.assertEqual('https://example.com/rss/', actual_rss_config.source_url)
        self.assertEqual(False, actual_rss_config.to_json)
        self.assertEqual(False, actual_rss_config.verbose)
        self.assertEqual(None, actual_rss_config.limit)
        self.assertEqual(datetime(2021, 11, 6, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc),
                         actual_rss_config.date)

    def test_date_arg_parse_positive_date_only(self):
        actual_rss_config = common_utils.parse_arguments(['--date=20211106'], Mock())
        self.assertEqual(None, actual_rss_config.source_url)
        self.assertEqual(False, actual_rss_config.to_json)
        self.assertEqual(False, actual_rss_config.verbose)
        self.assertEqual(None, actual_rss_config.limit)
        self.assertEqual(datetime(2021, 11, 6, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc),
                         actual_rss_config.date)

    def test_convert_datetime_to_timestamp_positive(self):
        actual = common_utils.convert_datetime_to_timestamp(datetime(2021, 10, 30))
        self.assertEqual(1635544800, actual)

    def test_convert_timestamp_to_datetime_positive(self):
        actual = common_utils.convert_timestamp_to_datetime(1635544800)
        self.assertEqual(datetime(2021, 10, 30), actual)

    def test_parse_date_from_rss_positive(self):
        actual = common_utils.parse_date_from_rss('Sun, 17 Oct 2021 11:03:45 +0300')
        self.assertEqual(datetime(2021, 10, 17, hour=8, minute=3, second=45, tzinfo=timezone.utc), actual)
