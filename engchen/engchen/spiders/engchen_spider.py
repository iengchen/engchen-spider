# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from engchen.items import EngchenItem

class EngchenSpider(Spider):
    name = "engchen"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?sort=newest"]

    def parse(self,response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = EngchenItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield  item
