# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['rs.olx.com.br/autos-e-pecas/carros-vans-e-utilitario']
    start_urls = ['http://rs.olx.com.br/autos-e-pecas/carros-vans-e-utilitario/']

    def parse(self, response):
        itens = response.xpath('//ul[@id="main-ad-list"]/li')
        for item in itens:
            self.log(item.xpath('./a/@href').extract_first())
