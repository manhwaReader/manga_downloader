    # Python program to read
    # json file

import scrapy
import json

class ChaptersSpider (scrapy.Spider):
    name = 'chapters'
    # Opening JSON file
    f = open('mangas.json')
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    for i in data:
        print(i)
    # Closing file
    f.close()
