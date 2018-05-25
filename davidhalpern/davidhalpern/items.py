# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DavidhalpernItem(scrapy.Item):
    # defining the names of the extracted items
    date_published = scrapy.Field()
    category = scrapy.Field()
    article_title = scrapy.Field()
    main_image = scrapy.Field()
    article = scrapy.Field()



    pass
