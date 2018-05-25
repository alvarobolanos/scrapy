# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BougainvilleaItem(scrapy.Item):
    # define the fields for your item here like:
    article = scrapy.Field()
    main_image = scrapy.Field()
    date_published = scrapy.Field()
    article_title = scrapy.Field()
    #url = scrapy.Field()
    pass
