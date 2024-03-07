from pathlib import Path
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class VozSpider(CrawlSpider):
    name = "voz"
    allowed_domains = ["voz.vn"]
    start_urls = ["https://voz.vn/t/tan-nuoc-tu-che-vo-cuc-cho-old-man-ngheo-kho.645434/"]
    rules = (
        Rule(LinkExtractor()),
    )
    count = 0

    def AA_parse(self, response, **kwargs):
        return self._parse_response(
            response=response,
            callback=self.parse_start_url,
            cb_kwargs=kwargs,
            follow=True,
        )

    def _parse(self, response, **kwargs):
        self.print_msg('______parse called')
        
        self.count += 1
        if self.count >= 10:
            print('\n\n\n==================================================');
            print('STOP ................')
            return

        parent1 = super()
        return parent1._parse(response, **kwargs)
        
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")

        # for link in self.link_extractor.extract_links(response):
        #     yield Request(link.url, callback=self.parse)        

    def _callback(self, response, **cb_kwargs):
        self.print_msg('_callback called')
        return super()._callback(response, **cb_kwargs)
    
    def parse(self, response, **kwargs):
        self.print_msg('parse called')

        self.count += 1
        if self.count >= 10:
            print('\n\n\n==================================================');
            print('STOP ................')
            return

    def print_msg(self, msg):
        print(f'\n\n\n\n===========================\n{msg}')
