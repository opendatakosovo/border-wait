import scrapy, datetime, re, json
from borderwait.items import BorderWaitItem
from scrapy.exceptions import DropItem

class BorderWaitSpider(scrapy.Spider):
    name = "borderwait"
    allowed_domains = ["mpb-ks.org"]
    start_urls = ["http://www.mpb-ks.org/qkmk/"]
    digits = re.compile("([0-9]+)")
    def parse(self, response):
        dt = response.xpath('//span[@class="time"]/text()').extract()[0]
        data = response.xpath('//div[@class="home-table"]//tr//td/text()').extract()
        border_crossings = list(self.chunks(data, 5))
        for bc in border_crossings:
            item = BorderWaitItem()
            item["date"] = datetime.datetime.strptime(dt, "%d.%m.%Y %H:%M")
            item["time"] = dt.split(' ')[1]
            item["border"] = bc[0]
            entry = self.conver_int(bc[1], bc)
            exit = self.conver_int(bc[2], bc)
            entryq = self.conver_int(bc[3], bc)
            exitq = self.conver_int(bc[4], bc)
            error = 'error'
            if entry == error or exit == error or entryq == error or exitq == error :
                continue
            else:
                item["entry"] = {'min':entry[0], 'max':entry[1]}
                item["exit"] = {'min':exit[0], 'max':exit[1]}
                item["entry_q"] = {'min':entryq[0], 'max':entryq[1]}
                item["exit_q"] = {'min': exitq[0], 'max':exitq[1]}
            yield item

    def conver_int(self, str_num, err_data):
        try:
            if '-' in str_num:
                num_array = [ex.replace(' ','') for ex in str_num.split('-')]
                num1 = self.digits.match(num_array[0])
                res = int(num1.group(1))
                num_array[0] = res
                num2 = self.digits.match(num_array[1])
                res = int(num2.group(1))
                num_array[1] = res
                return num_array
            else:
                num = self.digits.match(str_num)
                res = int(num.group(1))
                num_array = [res , res]
                return num_array
        except Exception as e:
            self.log('\nError processing %s : %s\n' % (json.dumps(err_data), str(e)))
            return 'error'

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
