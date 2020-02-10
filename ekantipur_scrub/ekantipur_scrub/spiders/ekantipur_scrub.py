import scrapy

class PostSpider(scrapy.Spider):
    name = 'news'

    start_urls = [
        'https://ekantipur.com/news/'
    ]

    def parse(self, response):
        for news in response.css('article'):
            yield{
                'title': news.css('.normal h2 a::text')[0].get(),
                'author': news.css('.normal a::text')[1].get(),
                #'date': news.css('.normal h2 a::text')[2].get(),
            }

        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)