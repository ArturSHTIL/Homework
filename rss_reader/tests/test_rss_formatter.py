import unittest
from unittest.mock import Mock
from rss_reader.representation import RssFormatter
from rss_reader.entities import RssFeed, RssItem
from datetime import datetime, timezone

def get_rss_feed_for_testing() -> "RssFeed":
    rss_feed = RssFeed('https://people.onliner.by/feed',
                       'Люди Onlíner',
                       'https://people.onliner.by/',
                       datetime(2021, 10, 17, hour=11, minute=3, second=45, tzinfo=timezone.utc),
                       'Люди Onlíner')
    rss_feed.add_item(RssItem(
        '14-летняя белоруска победила на престижном международном фестивале в Италии',
        'https://people.onliner.by/2021/10/17/beloruska-pobedila-na-festivale-v-italii',
        datetime(2021, 10, 17, hour=11, minute=3, second=45, tzinfo=timezone.utc),
        '14-летняя солистка продюсерского центра «Спамаш» Ксения Галецкая выиграла престижный детский вокальный конкурс sanremoJunior, сообщили в инстаграм-аккаунте центра. Ксения исполнила хит Who’s Loving You.Читать далее…'
    ))
    rss_feed.add_item(RssItem(
        'Матулям прысвячаецца. Спецвыпуск беларускіх шпаргалак',
        'https://people.onliner.by/2021/10/17/specvypusk-shpargalak-3',
        datetime(2021, 10, 17, hour=10, minute=0, second=8, tzinfo=timezone.utc),
        '14 кастрычніка многія беларусы адзначалі Дзень маці, таму сённяшні выпуск нашых традыцыйных шпаргалак прысвечаны мамам. Мы вырашылі паглядзець, як тэма адносін да мацеры адлюстравана ў прыказках, прымаўках ды параўнаннях — тым, што робіць наша маўленне больш багатым, яскравым і адметным. Запамінайце ўстойлівыя трапныя выразы і карыстайцеся імі пры нагодзе.Читать далее…'
    ))
    return rss_feed


class TestRssFormatter(unittest.TestCase):

    def test_get_rss_as_text_positive(self):
        actual = RssFormatter(get_rss_feed_for_testing(), Mock()).get_rss_as_text()

        self.assertEqual('''Rss feed title: Люди Onlíner
Rss feed link: https://people.onliner.by/
Rss feed description: Люди Onlíner
Rss feed date: 2021-10-17 11:03:45+00:00

title: 14-летняя белоруска победила на престижном международном фестивале в Италии
link: https://people.onliner.by/2021/10/17/beloruska-pobedila-na-festivale-v-italii
date: 2021-10-17 11:03:45+00:00
description: 14-летняя солистка продюсерского центра «Спамаш» Ксения Галецкая выиграла престижный детский вокальный конкурс sanremoJunior, сообщили в инстаграм-аккаунте центра. Ксения исполнила хит Who’s Loving You.Читать далее…

title: Матулям прысвячаецца. Спецвыпуск беларускіх шпаргалак
link: https://people.onliner.by/2021/10/17/specvypusk-shpargalak-3
date: 2021-10-17 10:00:08+00:00
description: 14 кастрычніка многія беларусы адзначалі Дзень маці, таму сённяшні выпуск нашых традыцыйных шпаргалак прысвечаны мамам. Мы вырашылі паглядзець, як тэма адносін да мацеры адлюстравана ў прыказках, прымаўках ды параўнаннях — тым, што робіць наша маўленне больш багатым, яскравым і адметным. Запамінайце ўстойлівыя трапныя выразы і карыстайцеся імі пры нагодзе.Читать далее…\n''', actual)

    def test_get_rss_as_json_positive(self):
        actual = RssFormatter(get_rss_feed_for_testing(), Mock()).get_rss_as_json()

        self.assertEqual('''{
    "rss_title": "Люди Onlíner",
    "rss_link": "https://people.onliner.by/",
    "rss_description": "Люди Onlíner",
    "rss_pub_date": "2021-10-17T11:03:45+00:00",
    "rss_items": [
        {
            "title": "14-летняя белоруска победила на престижном международном фестивале в Италии",
            "link": "https://people.onliner.by/2021/10/17/beloruska-pobedila-na-festivale-v-italii",
            "date": "2021-10-17T11:03:45+00:00",
            "description": "14-летняя солистка продюсерского центра «Спамаш» Ксения Галецкая выиграла престижный детский вокальный конкурс sanremoJunior, сообщили в инстаграм-аккаунте центра. Ксения исполнила хит Who’s Loving You.Читать далее…"
        },
        {
            "title": "Матулям прысвячаецца. Спецвыпуск беларускіх шпаргалак",
            "link": "https://people.onliner.by/2021/10/17/specvypusk-shpargalak-3",
            "date": "2021-10-17T10:00:08+00:00",
            "description": "14 кастрычніка многія беларусы адзначалі Дзень маці, таму сённяшні выпуск нашых традыцыйных шпаргалак прысвечаны мамам. Мы вырашылі паглядзець, як тэма адносін да мацеры адлюстравана ў прыказках, прымаўках ды параўнаннях — тым, што робіць наша маўленне больш багатым, яскравым і адметным. Запамінайце ўстойлівыя трапныя выразы і карыстайцеся імі пры нагодзе.Читать далее…"
        }
    ]
}''', actual)


if __name__ == '__main__':
    unittest.main()
