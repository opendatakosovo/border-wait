import scrapy, datetime
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
            item["date"] = datetime.datetime.strptime(dt, "%d.%m.%Y %H:%M")
            item["time"] = dt.split(' ')[1]
            item["border"] = bc[0].replace(' ', '')
            entry = [int(d.replace(' ', '')) for d in bc[1].split('-')]
            item["entry"] = {'min':entry[0], 'max':entry[1]}
            exit = [int(d.replace(' ', '')) for d in bc[2].split('-')]
            item["exit"] = {'min':exit[0], 'max':exit[1]}
            entryq = []
            if '-' in bc[3]:
                entryq = [int(en.replace(' ','')) for en in bc[3].split('-')]
            else:
                entryq = [int(bc[3]),int(bc[3])]
            item["entry_q"] = {'min':entryq[0], 'max':entryq[1]}
            exitq = []
            if '-' in bc[4]:
                exitq = [int(ex.replace(' ','')) for ex in bc[4].split('-')]
            else:
                exitq = [int(bc[4]), int(bc[4])]
            item["exit_q"] = {'min': exitq[0], 'max':exitq[1]}
            yield item

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
