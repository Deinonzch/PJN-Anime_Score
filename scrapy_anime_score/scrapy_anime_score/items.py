# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAnimeScoreItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    score = scrapy.Field()
    type = scrapy.Field()
    genres = scrapy.Field()
    studios = scrapy.Field()
    main_actors = scrapy.Field()
    original_creator = scrapy.Field()
    producer = scrapy.Field()
    script = scrapy.Field()
    director = scrapy.Field()
    animation_director = scrapy.Field()
    adr_director = scrapy.Field()
    sound_director = scrapy.Field()
    music = scrapy.Field()
    url = scrapy.Field()

class urlItem(scrapy.Item):
    url = scrapy.Field()
