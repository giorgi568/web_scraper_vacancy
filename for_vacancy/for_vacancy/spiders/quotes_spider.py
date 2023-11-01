from pathlib import Path

import scrapy


class VacancySpider(scrapy.Spider):
    name = "vacancy"
    searchWord = "იურისტი"
    start_urls = [
    # f'https://www.hr.ge/search-posting?q={searchWord}&l=%5B1%5D&p=1&pg=1&cc=909'
    f'https://www.hr.ge/search-posting?q={searchWord}&l=%5B1%5D&p=2&pg=1&cc=693'
    ]

    def parse(self, response):
        for link in response.css("a.title ::attr(href)").getall():
            job_link = response.urljoin(link)
            yield scrapy.Request(url=job_link, callback=self.parse_job)
    

    def parse_job(self, response):
        job_data = {
            "title" : response.css("div.ann-title-container__text::text").get(),
            "company" : response.css("a.company-name__link::text").get(),
            "ganakveti" : response.css("div.details ul.list li.list__item::text").get(),
            # "salary" : response.css("div.details ul.list li.list__item.ng-star-inserted span:nth-child(2)::text").get()
        }

        yield job_data


        # for title in response.css("div.title--bold-desktop::text").getall():
        #     yield {
        #         "title" : title
        #     }

        # body_page = response.css("a.title") 
        # a.title ::attr(href)