import unittest
import rss_reader
from io import StringIO
from unittest.mock import Mock, patch


class TestArgumentParsing(unittest.TestCase):

    def test_only_required_args_parse_positive(self):
        actual = rss_reader.parse_arguments(['https://example.com/rss/'], Mock())
        self.assertEqual(len(actual), 4)
        self.assertEqual('https://example.com/rss/', actual[0])
        self.assertEqual(False, actual[1])
        self.assertEqual(False, actual[2])
        self.assertEqual(None, actual[3])

    def test_limit_args_parse_positive(self):
        actual = rss_reader.parse_arguments(['https://example.com/rss/', '--limit=2'], Mock())
        self.assertEqual(len(actual), 4)
        self.assertEqual('https://example.com/rss/', actual[0])
        self.assertEqual(False, actual[1])
        self.assertEqual(False, actual[2])
        self.assertEqual(2, actual[3])

    def test_json_arg_parse_positive(self):
        actual = rss_reader.parse_arguments(['https://example.com/rss/', '--json'], Mock())
        self.assertEqual(len(actual), 4)
        self.assertEqual('https://example.com/rss/', actual[0])
        self.assertEqual(True, actual[1], '--json arg should be True')
        self.assertEqual(False, actual[2])
        self.assertEqual(None, actual[3])

    def test_verbose_arg_parse_positive(self):
        actual = rss_reader.parse_arguments(['https://example.com/rss/', '--verbose'], Mock())
        self.assertEqual(len(actual), 4)
        self.assertEqual('https://example.com/rss/', actual[0])
        self.assertEqual(False, actual[1])
        self.assertEqual(True, actual[2], '--verbose arg should be True')
        self.assertEqual(None, actual[3])

    def test_arg_parse_negative(self):
        with patch('sys.stderr', new_callable=StringIO) as mocked_stderr:
            with self.assertRaises(SystemExit) as cm:
                rss_reader.parse_arguments([], Mock())
            self.assertEqual(cm.exception.code, 2)
            self.assertIn('the following arguments are required: source', mocked_stderr.getvalue())
