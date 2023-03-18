    # Python program to read
    # json file

import scrapy
import json

class ChaptersSpider (scrapy.Spider):
    name = 'chapters'
    
    def start_requests(self):
        # Opening JSON file
        f = open('mangas.json')
        # returns JSON object as a dictionary
        datas = json.load(f)
        # Iterating through the json list
        print(datas)
        # Closing file
        f.close()

        for data in datas:
            yield scrapy.Request(url= 'https://www.mreader.co/reader/en/'+data.url.split('/')[2]+'-'+data.chapter.lower(), callback=self.parse)

    # def parse(self, response):
    #     for manga in response.css('img'):
