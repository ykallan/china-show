# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhanhuiItem(scrapy.Item):

    名称 = scrapy.Field()
    场馆 = scrapy.Field()
    日期 = scrapy.Field()
    主办方 = scrapy.Field()
    地址 = scrapy.Field()
    城市 = scrapy.Field()
    详情 = scrapy.Field()

# 名称 场馆 日期 主办方 地址 城市 详情