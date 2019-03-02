# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader.processor import Compose, MapCompose



class DataFetcherSpider(scrapy.Spider):
    name = 'data_fetcher'
    #allowed_domains = ['https://www.imdb.com/title/tt0111161']
    #start_urls = ['https://www.imdb.com/title/tt0111161/']

    allowed_domains = []
    start_urls = []

    url_file = open('E:\work_area\python\Scrapy\IMDB\movies_url.csv')
    for i in url_file:
        u = i.split('\n')
        start_urls.append(u[0])

    def parse(self, response):

        name =  response.xpath('//*[@class="title_wrapper"]/h1/text()').extract_first()
        name = ' '.join(name.split())
        Link =  response.xpath('//*[@rel="canonical"]/@href').extract_first()
        release_yr = response.xpath('//*[@class="title_wrapper"]/h1/span[@id="titleYear"]/a/text()').extract_first()
        IMDB_rating = response.xpath('//*[@itemprop="ratingValue"]/text()').extract_first()
        reviewers = response.xpath('//*[@itemprop="ratingCount"]/text()').extract_first()
        censor_board_rating = response.xpath('//*[@class="subtext"]/text()').extract_first()
        censor_board_rating = ''.join(censor_board_rating.split())
        movie_length = response.xpath('//*[@class="subtext"]/time/text()').extract_first()
        movie_length = ''.join(movie_length.split())
        Genre_1 = response.xpath('//*[@class="see-more inline canwrap"][2]/a[1]/text()').extract_first()
        Genre_2 = response.xpath('//*[@class="see-more inline canwrap"][2]/a[2]/text()').extract_first()
        Genre_3 = response.xpath('//*[@class="see-more inline canwrap"][2]/a[3]/text()').extract_first()
        Genre_4 = response.xpath('//*[@class="see-more inline canwrap"][2]/a[4]/text()').extract_first()
        release_date = response.xpath('//*[@title="See more release dates"]/text()').extract_first()
        release_date = ' '.join(release_date.split())
        summary = response.xpath('//*[@class="summary_text"]/text()').extract_first()
        summary = ' '.join(summary.split())
        director = response.xpath('//*[@class="credit_summary_item"][1]/a/text()').extract_first()
        writer_1 = response.xpath('//*[@class="credit_summary_item"][2]/a[1]/text()').extract_first()
        writer_2 = response.xpath('//*[@class="credit_summary_item"][2]/a[2]/text()').extract_first()
        writer_3 = response.xpath('//*[@class="credit_summary_item"][2]/a[3]/text()').extract_first()
        star_1 = response.xpath('//*[@class="credit_summary_item"][3]/a[1]/text()').extract_first()
        star_2 = response.xpath('//*[@class="credit_summary_item"][3]/a[2]/text()').extract_first()
        star_3 = response.xpath('//*[@class="credit_summary_item"][3]/a[3]/text()').extract_first()
        star_4 = response.xpath('//*[@class="credit_summary_item"][3]/a[4]/text()').extract_first()
        star_5 = response.xpath('//*[@class="credit_summary_item"][3]/a[5]/text()').extract_first()
        keyword_1 = response.xpath('//*[@class="see-more inline canwrap"][1]/a[1]/span[@class="itemprop"]/text()').extract_first()
        keyword_2 = response.xpath('//*[@class="see-more inline canwrap"][1]/a[2]/span[@class="itemprop"]/text()').extract_first()
        keyword_3 = response.xpath('//*[@class="see-more inline canwrap"][1]/a[3]/span[@class="itemprop"]/text()').extract_first()
        keyword_4 = response.xpath('//*[@class="see-more inline canwrap"][1]/a[4]/span[@class="itemprop"]/text()').extract_first()
        keyword_5 = response.xpath('//*[@class="see-more inline canwrap"][1]/a[5]/span[@class="itemprop"]/text()').extract_first()
        keywords = keyword_1 +' | '+ keyword_2 +' | '+ keyword_3 +' | '+ keyword_4 +' | '+ keyword_5

        checker_list = response.xpath('//*[@id="titleDetails"]/div[@class="txt-block"]/h4/text()').extract()

        L=[]
        for i in range(0,len(checker_list)):
            zz = checker_list[i]
            L.append(zz)

        if "Budget:" in L:
            Budget_index = L.index("Budget:")
            Budget_index = Budget_index+1
            budget = response.xpath('//*[@class="txt-block"][{}]/text()'.format(Budget_index))[1].extract()
            budget = ' '.join(budget.split())
            budget = budget.replace(',','')
            budget = budget.replace('$','')
        else:
            budget = "NOT AVAILABLE"
        yield budget

        if "Gross USA:" in L:
            Gross_USA_index = L.index("Gross USA:")
            Gross_USA_index = Gross_USA_index+1
            Gross_USA = response.xpath('//*[@class="txt-block"][{}]/text()'.format(Gross_USA_index))[1].extract()
            Gross_USA = ' '.join(Gross_USA.split())
            Gross_USA = Gross_USA.replace(',','')
            Gross_USA = Gross_USA.replace('$','')
        else:
            Gross_USA = "NOT AVAILABLE"
        yield Gross_USA



        if "Cumulative Worldwide Gross:" in L:
            worldwide_gross_index = L.index("Cumulative Worldwide Gross:")
            worldwide_gross_index = worldwide_gross_index+1
            worldwide_gross = response.xpath('//*[@class="txt-block"][{}]/text()'.format(worldwide_gross_index))[1].extract()
            worldwide_gross = ' '.join(worldwide_gross.split())
            worldwide_gross = worldwide_gross.replace(',','')
            worldwide_gross = worldwide_gross.replace('$','')
        else:
            worldwide_gross = "NOT AVAILABLE"
        yield worldwide_gross


        if "Production Co:" in L:
            Production_index = L.index("Production Co:")
            Production_index = Production_index+1
            Production_co = response.xpath('//*[@class="txt-block"][{}]/a/text()'.format(Production_index)).extract_first()
            Production_co = ' '.join(Production_co.split())
        else:
            Production_co = "NOT AVAILABLE"
        yield Production_co


        print("####################################################################")
        print('name=',name)
        print('link=',Link)
        print('release_yr=',release_yr)
        print('IMDB_rating=',IMDB_rating)
        print("reviewers=",reviewers)
        print("censor_board_rating=",censor_board_rating)
        print("movie_length=",movie_length)
        print('Genre_1=',Genre_1)
        print('Genre_2=',Genre_2)
        print('Genre_3=',Genre_3)
        print('Genre_4=',Genre_4)
        print('release_date=',release_date)
        print('summary=',summary)
        print('director=',director)
        print('writer_1=',writer_1)
        print('writer_2=',writer_2)
        print('writer_3=',writer_3)
        print('star_1=',star_1)
        print('star_2=',star_2)
        print('star_3=',star_3)
        print('star_4=',star_4)
        print('star_5=',star_5)
        print('Keywords=',keywords)
        print('budget=',budget)
        print('Gross_USA=',Gross_USA)
        print('Cumulative Worldwide Gross=',worldwide_gross)
        print('production_co=',Production_co)
        print("####################################################################")

        yield{'Name of the movie':name,
              'Link':Link,
              'Year released':release_yr,
              'IMDB rating': IMDB_rating,
              'Number of reviewers': reviewers,
              'Censor board rating': censor_board_rating,
              'Length of the movie': movie_length,
              'Genre 1': Genre_1,
              'Genre 2': Genre_2,
              'Genre 3': Genre_3,
              'Genre 4': Genre_4,
              'Release date': release_date,
              'story summary': summary,
              'Director Name': director,
              'Writer 1': writer_1,
              'Writer 2': writer_2,
              'Writer 3': writer_3,
              'Star 1': star_1,
              'Star 2': star_2,
              'Star 3': star_3,
              'Star 4': star_4,
              'Star 5': star_5,
              'Plot Keywords list': keywords,
              'Budget': budget,
              'Gross USA': Gross_USA,
              'Cumulative worlwide Gross': worldwide_gross,
              'Production company': Production_co
        }
