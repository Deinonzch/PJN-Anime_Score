import scrapy
import re
from scrapy_anime_score.items import *

class anime_url_get(scrapy.Spider):
    name = "anime_url_get"
    allowed_domains = ['myanimelist.net']
    start_urls = ['https://myanimelist.net/anime/producer']

    def parse(self, response):
        item = urlItem()
        item2 = urlItem()

        item['url'] = response.xpath('//div[@class="genre-list al"]/a/@href').extract()
        list = []
        for i in item['url']:
            list.append('//div/a[@href="' + i + '"]/text()|')
        item2['url'] = list
        yield item2