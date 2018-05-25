import scrapy
from davidhalpern.items import DavidhalpernItem
from datetime import datetime
import re

class DavidhalpernBlog(scrapy.Spider):
    name = 'blog_scrape'

    # First start Url
    start_urls= ['http://www.davidhalpernmd.com/blog/']

    npages = 5

    for i in range(1,npages):
        start_urls.append('http://www.davidhalpernmd.com/blog/page/'+str(i)+'/')

    def parse(self, response):
        for href in response.xpath("//h2[contains(@class, 'entry-title')]/a/@href"):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self,response):
        item = DavidhalpernItem()

        # date_updated
        item['date_published'] = response.xpath("//abbr[contains(@class, 'published')]/@title").extract()

        # category
        item['category'] = response.xpath("//span[contains(@class, 'cmsms_category')]//a/text()").extract()

        # article_title
        item['article_title'] = response.xpath("//h2[contains(@class, 'entry-title')]/text()").extract()

        # main_image
        item['main_image'] = response.xpath("//span[@class = 'p_img_container']/img/@src")

        # article
        text = response.xpath("//div[@class = 'entry-content']//span/text()").extract()
        item['article'] = ''.join(text)

        yield item