import scrapy

from borderwait.items import BorderWaitItem

class BorderWaitSpider(scrapy.Spider):
    name = "borderwait"
    allowed_domains = ["mpb-ks.org"]
    start_urls = ["http://www.mpb-ks.org/qkmk/"]

    def parse(self, response):
        dt = response.xpath('//span[@class="time"]/text()').extract()[0]
        data = response.xpath('//div[@class="home-table"]//tr//td/text()').extract()
        border_crossings = list(self.chunks(data, 5))
        for bc in border_crossings:
            item = BorderWaitItem()
            item['date'] = dt.split(' ')[0]
            item['time'] = dt.split(' ')[1]
            item['border'] = bc[0]
            item['entry'] = bc[1].replace(' ', '').replace('min','')
            item['exit'] = bc[2].replace(' ', '').replace('min','')
            item['entry_q'] = bc[3].replace(' ', '').replace('m','')
            item['exit_q'] = bc[4].replace(' ', '').replace('m','')
            yield item

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
