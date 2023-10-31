from pathlib import Path

import scrapy


class VacancySpider(scrapy.Spider):
    name = "vacancy"
    searchWord = "იურისტი"
    start_urls = [
    f'https://www.hr.ge/search-posting?q={searchWord}&l=%5B1%5D&p=1&pg=1&cc=909'
    ]

    def parse(self, response):
        for title in response.css("div.title--bold-desktop::text").getall():
            yield {
                "title" : title
            }

        # body_page = response.css("a.title")