# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "transporte"
    allowed_domains = ["www.mininterior.gov.ar"]
    start_urls = (
        'http://www.mininterior.gov.ar/web_transporte/colectivos.php',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2]
        urls = response.xpath('//ul/li/a/@href').extract()
        for url in urls:
        	yield scrapy.Request('http://www.mininterior.gov.ar/web_transporte/' +url, callback=self.parse)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)