# -*- coding: utf-8 -*-
# Author: ChinaHackers

import scrapy
from ..items import MovieItem



class DyttSpider(scrapy.Spider):

    name = 'dytt'
    allowed_domains = ['dytt8.net']
    start_urls = ['https://www.dytt8.net']

    # 开始请求
    def start_requests(self):
        base_url = 'https://www.dytt8.net/html/gndy/{}/index.html'
        categories = ['china', 'rihan', 'oumei', 'dyzz']
        for category in categories:
            yield scrapy.Request(base_url.format(category), callback=self.parse)


    # 开始解析
    def parse(self, response):
        detail_urls = response.xpath('//a[@class="ulink"]/@href').extract()
        detail_urls = [url for url in detail_urls if 'index' not in url]
        # print(detail_urls)

        for url in detail_urls:
            # 发起新的request
            yield scrapy.Request(response.urljoin(url), callback=self.detail)
        # 下一页链接
        next_page = response.xpath('.//a[contains(text(),"下一页")]/@href').extract_first()

        if next_page is not None:       # 如果下一页没有, urljoin: 返回的url链接下一页的url，组成新的url

            next_page = response.urljoin(next_page)

            # 发起新的request
            yield scrapy.Request(next_page, callback=self.parse)


    # 详情页面
    def detail(self, response):

        item = MovieItem()

        # 获取下载ftp链接
        download_url_list = response.xpath('//a/text()').re('ftp.*')
        for download_url in download_url_list:
            item['download_url'] = download_url
            yield item