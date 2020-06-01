# -*- coding: utf-8 -*-
# 中国展会网
import scrapy
from ..items import ZhanhuiItem


class ZhSpider(scrapy.Spider):
    name = 'zh'
    start_uuu = 'http://www.china-show.net/exhibit/search-htm-page-1-kw--fields-0-fromdate-20200601-todate--catid-0-process-0-order-0-x-49-y-17.html'
    base_url = 'http://www.china-show.net'

    def __init__(self):
        super(ZhSpider, self).__init__()
        self.start_req_url = input('请输入需要爬取的网页链接，可直接回车继续爬取：')

    def start_requests(self):
        if len(self.start_req_url) < 10:
            yield scrapy.Request(url=self.start_uuu,callback=self.parse)
        else:
            yield scrapy.Request(url=self.start_req_url, callback=self.parse)

    def parse(self, response):
        url_list = response.xpath('//td[@align="left"]/ul/li/a/@href').extract()
        page = response.xpath('//div[@class="pages"]/strong/text()').extract_first()
        for i in range(len(url_list)):

            meta = {
                'page': page
            }
            yield scrapy.Request(url=url_list[i], callback=self.parse_detail, meta=meta)

        next_page = response.xpath('//a[@title="下一页"]/@href').extract_first()

        yield scrapy.Request(url=self.base_url+next_page, callback=self.parse)

    def parse_detail(self, response):
        item = ZhanhuiItem()

        page = response.meta['page']
        title = response.xpath('//h1[@class="title"]/text()').extract_first()
        data = response.xpath('//table/tr[1]/td[2]/text()').extract_first()
        loc = response.xpath('//table/tr[2]/td[2]/text()').extract_first()
        address = response.xpath('//table/tr[3]/td[2]/text()').extract_first()
        name = response.xpath('//table/tr[4]/td[2]/text()').extract_first()
        host = response.xpath('//table/tr[5]/td[2]/text()').extract_first()
        contents = response.xpath('//div[@class="pd10 lh18 px13"]//*/text()').extract()
        content = ''
        for con in contents:
            if con != '\r\n':
                con.replace('\r', '').replace('\n', '').replace(' ', '')
                if len(con) != 0:
                    content += con

        item['名称'] = title
        item['日期'] = data
        item['城市'] = loc
        item['地址'] = address
        item['场馆'] = name
        item['主办方'] = host
        item['详情'] = content
        # 名称 场馆 日期 主办方 地址 城市 详情
        yield item
        print('这是第', page, '页的信息')

