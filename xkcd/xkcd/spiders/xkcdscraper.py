# -*- coding: utf-8 -*-
import scrapy
from xkcd.items import XkcdItem

class XkcdSpider(scrapy.Spider):
    name = "xkcdscraper"
    allowed_domains = ["xkcd.com"]
    start_urls = (
        'http://www.xkcd.com/1/',
    )

    def parse(self, response):
    	img_url = response.xpath('//*[@id="comic"]/img/@src').extract_first()
      
      	image = XkcdItem()
       	image['image_urls'] = ['http:' + img_url]
       	yield image

       	next_page = response.xpath('//*[@id="middleContainer"]/ul[2]/li[4]/a/@href').extract_first()
      	if next_page != '#':
      		next_page = response.urljoin(next_page)
      		yield scrapy.Request(next_page, callback = self.parse)
