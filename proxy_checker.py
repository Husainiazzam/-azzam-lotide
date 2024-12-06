import scrapy

class ProxyCheckerSpider(scrapy.Spider):
    name = 'proxy_checker'
    start_urls = ['https://www.google.com']

    def start_requests(self):
        for url in self.start_urls:
            for proxy in ['http://qawjregv755qody-country-us-session-ug6ryu1w4m-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060', 
'http://qawjregv755qody-country-us-session-2ly888f74v-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-2xul6i16g5-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-3gxwg5m6h0-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-jrx5j651iz-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-e2p9igdpdm-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-nmt8gy2dc8-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-yzx6uewek9-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-0pje5i92pt-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',
'http://qawjregv755qody-country-us-session-m45bvwqedu-lifetime-120:dbaohhohalujwqd@51.159.85.23:6060',]:
                yield scrapy.Request(url=url, meta={'proxy': proxy}, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print(f"Proxy {response.meta['proxy']} is active")
        else:
            print(f"Proxy {response.meta['proxy']} is inactive or there was an error")
