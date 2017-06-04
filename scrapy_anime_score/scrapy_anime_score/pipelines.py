# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy_anime_score.items import *

'''
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
'''


def delete_white_char_person(list):
    normalize_list = []
    for l in list:
        li = l[0].replace(', ', '_')
        normalize_list.append(li.replace(' ', '_'))
    return normalize_list

def delete_white_char(list):
    normalize_list = []
    for l in list:
        normalize_list.append(l.replace(' ', '_'))
    return normalize_list

def delete_white_char_actors(list):
    normalize_list = []
    for l in list:
        li = l.replace(', ', '_')
        normalize_list.append(li.replace(' ', '_'))
    return normalize_list

def one_string(anime):
    string = anime['score'] + " |type " + anime['type'] + " |genres "
    for a in anime['genres']:
        string = string + a + " "
    if anime['studios'] != []:
        string = string + "|studios "
        for a in anime['studios']:
            string = string + a + " "
    if anime['main_actors'] != []:
        string = string + "|main_actors "
        for a in anime['main_actors']:
            string = string + a + " "
    return string

class ScrapyAnimeScorePipeline(object):
    def __init__(self):
        self.file = codecs.open('anime_score_data', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if item['score'] != [] and item['score'] != 'N/A' and item['type'] != [] and item['genres'] != [] and item['studios'] != [] and item['main_actors'] != []:
            anime = ScrapyAnimeScoreItem()
            anime['score'] = item['score']
            string = anime['score']
            anime['name'] = item['name']
            string = string + " '" + anime['name'].replace(' ', '_')
            anime['type'] = item['type']
            string = string + " |type " + anime['type']
            anime['genres'] = delete_white_char(item['genres'])
            string = string + " |genres "
            for a in anime['genres']:
                string = string + a + " "
            anime['studios'] = delete_white_char(item['studios'])
            string = string + "|studios "
            for a in anime['studios']:
                string = string + a + " "
            anime['main_actors'] = delete_white_char_actors(item['main_actors'])
            string = string + "|main_actors "
            for a in anime['main_actors']:
                string = string + a + " "
            if item['original_creator'] != []:
                anime['original_creator'] = delete_white_char_person(item['original_creator'])
                string = string + "|original_creator "
                for a in anime['original_creator']:
                    string = string + a + " "
            if item['producer'] != []:
                anime['producer'] = delete_white_char_person(item['producer'])
                string = string + "|producer "
                for a in anime['producer']:
                    string = string + a + " "
            if item['script'] != []:
                anime['script'] = delete_white_char_person(item['script'])
                string = string + "|script "
                for a in anime['script']:
                    string = string + a + " "
            if item['director'] != []:
                anime['director'] = delete_white_char_person(item['director'])
                string = string + "|director "
                for a in anime['director']:
                    string = string + a + " "
            if item['animation_director'] != []:
                anime['animation_director'] = delete_white_char_person(item['animation_director'])
                string = string + "|animation_director "
                for a in anime['animation_director']:
                    string = string + a + " "
            if item['adr_director'] != []:
                anime['adr_director'] = delete_white_char_person(item['adr_director'])
                string = string + "|adr_director "
                for a in anime['adr_director']:
                    string = string + a + " "
            if item['sound_director'] != []:
                anime['sound_director'] = delete_white_char_person(item['sound_director'])
                string = string + "|sound_director "
                for a in anime['sound_director']:
                    string = string + a + " "
            if item['music'] != []:
                anime['music'] = delete_white_char_person(item['music'])
                string = string + "|music "
                for a in anime['music']:
                    string = string + a + " "
            string = string + "\n"
            # build your row to export, then export the row
            # todo send to api
            self.file.write(string)
            return string

    def spider_closed(self, spider):
        self.file.close()