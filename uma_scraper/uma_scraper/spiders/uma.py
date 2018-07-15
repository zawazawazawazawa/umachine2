# -*- coding: utf-8 -*-
import scrapy


class UmaSpider(scrapy.Spider):
    name = 'uma'
    allowed_domains = ['netkeiba.com']
    # ネット競馬データベース　レース　詳細検索
    start_urls = ['http://db.netkeiba.com/?pid=race_search_detail']

    def parse(self, response):
        course = input("競争種別\n芝:1、ダート:2\n：")
        track = input("競馬場\n札幌:1、函館:2、福島:3、新潟:4、東京:5、\n中山:6、中京:7、京都:8、阪神:9、小倉:10\n:")
        race_class = input("クラス\nG1:1、G2:2、G3:3、1600万:4、1000万:5、500万:6、新馬:7、未勝利:8\n:")
        distance = input("距離 (ｍ、半角英数)\n:")
        
