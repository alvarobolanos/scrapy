# -*- coding: utf-8 -*-
import scrapy
from bougainvillea.items import BougainvilleaItem
from datetime import datetime
import re


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['www.lookandfeelbetter.com']
    start_urls = ['http://www.lookandfeelbetter.com']

    n = 11

    for i in range(0,n):
        start_urls.append('http://www.lookandfeelbetter.com/blog?page='+str(i)+'/')

    def parse(self, response):

        for href in response.xpath("//div[@class='view-content']//span[@class='field-content']//a/@href"):
            url = 'http://www.lookandfeelbetter.com' + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self,response):
        item = BougainvilleaItem()

        # article_title

        item['article_title'] = response.xpath("//h1/text()").extract()

        # date_published

        item['date_published'] = ((response.xpath("//p[@class='submitted']/text()").extract())[0].strip('\n')).strip(' ')[8:]

        # main_image

        item['main_image'] = 'http://www.lookandfeelbetter.com' + (str(response.xpath("//div[@class='field-item even']//img/@src").extract()).strip("['")).strip("']")

        # article

        text = response.xpath("//div[@class='field-item even']/p/text()").extract()
        item['article'] = ''.join(text)

        yield item
