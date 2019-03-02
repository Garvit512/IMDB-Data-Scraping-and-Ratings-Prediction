# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from urllib import parse


class Page250Spider(scrapy.Spider):
    name = 'page_250'
    allowed_domains = ['https://www.imdb.com/chart/top?ref_=nv_mv_250']
    start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250/']

    def parse(self, response):
        link_250 = response.xpath('//*[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
        for i in link_250:
            url_itterator = scrapy.Request(urljoin('https://www.imdb.com/chart/top?ref_=nv_mv_250', i[1:]),callback=self.parse_url)
            yield {'movie urls':url_itterator}


    def parse_url(self, response):
           print("error encountered")
