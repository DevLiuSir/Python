# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 明确需要抓取的目标数据
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    download_url = scrapy.Field()
