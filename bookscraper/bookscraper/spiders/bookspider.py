import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        quotes = response.css("div.quote")
        with open("quotes.txt", 'a', encoding='utf-8') as f:
            for quote in quotes:
                text = quote.css("span.text::text").get()
                f.write(text + "\n")    
            
        
            next_page = response.css("li.next a::attr(href)").get() 
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

