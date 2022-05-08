# -*- coding: utf-8 -*-
import scrapy


class TableSpider(scrapy.Spider):
    name = 'table'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table = response.xpath('//table[contains(@class,"wikitable sortable")]')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            rank = tr.xpath('.//td[1]/text()').extract_first().strip()
            city = tr.xpath('.//td[2]//text()').extract_first()
            state = tr.xpath('.//*[@class="flagicon"]/following-sibling::a/text()|'
                            './/*[@class="flagicon"]/following-sibling::text()').extract_first().strip()
            
            yield {
                'rank': rank,
                'city': city,
                'state': state
            }