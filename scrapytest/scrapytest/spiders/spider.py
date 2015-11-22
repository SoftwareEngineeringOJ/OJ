from scrapy.contrib.spiders import CrawlSpider

class spyyyyy(CrawlSpider):
    name = "ppp"
    start_urls = ["http://www.bnuoj.com/v3/problem.php"]
    def parse(self,response):
        print response.body

