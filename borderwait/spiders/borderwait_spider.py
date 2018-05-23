import scrapy, datetime, re, json
from borderwait.items import BorderWaitItem
from scrapy.exceptions import DropItem

class BorderWaitSpider(scrapy.Spider):
    name = "borderwait"
    allowed_domains = ["mpb.rks-gov.net"]
    start_urls = ["https://mpb.rks-gov.net/QKMK.aspx"]
    digits = re.compile("([0-9]+)")

    def parse(self, response):
        '''
            SCRAPING DATA
        '''
        raw_datetime = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_dtvBaneri_Majtas_lblBaneri_Djathtas"]/p[3]/span/strong/text()').extract()[0]
        data = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_dtvBaneri_Majtas_lblBaneri_Djathtas"]/table[1]/tbody/tr[position()>1]/td/text()').extract()
        border_crossings = list(self.chunks(data, 5))

        '''
            PROCESSING BORDER DATA
        '''
        for bc in border_crossings:
            # Creating new instance of BorderWaitItem
            item = BorderWaitItem()

            '''
                Populating the item instance
            '''
            # Border Name
            item["border"] = bc[0]

            # Datetime
            item['date'] = self.process_and_format_datetime(raw_datetime)
            # item['date'] = dt.isoformat()

            # Time
            item['time'] = raw_datetime[37:]

            # Border entry and exit (min)
            entry = self.conver_int(bc[1].strip(), bc)
            exit = self.conver_int(bc[2].strip(), bc)

            # Border entry and exit traffic jam (meters)
            entryq = self.conver_int(bc[3].strip(), bc)
            exitq = self.conver_int(bc[4].strip(), bc)

            error = 'error'
            if entry == error or exit == error or entryq == error or exitq == error:
                continue
            else:
                item["entry"] = {'min': entry[0], 'max': entry[1]}
                item["exit"] = {'min': exit[0], 'max': exit[1]}
                item["entry_q"] = {'min': entryq[0], 'max': entryq[1]}
                item["exit_q"] = {'min': exitq[0], 'max': exitq[1]}
            yield item

    '''
        PROCESSING INTEGERS
    '''
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
                num_array = [res, res]
                return num_array
        except Exception as e:
            self.log('\nError processing %s : %s\n' % (json.dumps(err_data), str(e)))
            return 'error'

    '''
        PROCESSING DATETIME
    '''
    def process_and_format_datetime(self, raw_datetime):
        # Getting only the date from the string
        date = raw_datetime[18:28]
        # Getting only the time from the string
        time = raw_datetime[37:]

        # Merging date and time together
        formatted_datetime = date + ' ' + time

        # Final formatted datetime
        final_formatted_datetime = datetime.datetime.strptime(formatted_datetime, "%d.%m.%Y %H:%M")

        return final_formatted_datetime

    def chunks(self, l, n):
            """Yield successive n-sized chunks from l."""
            for i in range(0, len(l), n):
                yield l[i:i + n]
