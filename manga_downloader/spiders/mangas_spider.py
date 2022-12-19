import scrapy

class MangasSpider(scrapy.Spider):
    name = "mangas"

    def start_requests(self):
        urls = ['https://www.mreader.co/jumbo/manga/',
                'https://www.mreader.co/jumbo/manga/?results=2&filter=All',
                'https://www.mreader.co/jumbo/manga/?results=3&filter=All',
                'https://www.mreader.co/jumbo/manga/?results=4&filter=All',
                'https://www.mreader.co/jumbo/manga/?results=5&filter=All',
                'https://www.mreader.co/jumbo/manga/?results=6&filter=All'
                ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for manga in response.css('li.novel-item'):
            url = manga.css('a.list-body::attr(href)').get()
            name = manga.css('a.list-body::attr(title)').get()
            chapter = manga.css('a.list-body div h5.chapter-title::text').get()
            if (url != None and name != None):
                data = dict(url=url, name=name.replace("\u2026", "...").replace("\u2019", "'").replace("\u00c9", "E")
                .replace("\u00e9", "e").replace("\u2764\ufe0f", "*"), chapter=chapter.split('\n')[1])
                yield data
        