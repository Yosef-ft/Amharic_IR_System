import scrapy
import urllib.request
import os

class PdfscraperSpider(scrapy.Spider):
    name = "pdfscraper"
    allowed_domains = ["allaboutethio.com"]
    start_urls = ["https://allaboutethio.com/amharic-books.html"]

    def parse(self, response):

        categories = response.css('table tr th p a::attr(href)').getall()

        for category in categories:
            
            category_url = 'https://allaboutethio.com/' + category

            category_name = category.split('.')[0]


            yield response.follow(category_url, callback= self.parse_cat_page, meta={'category_name': category_name})
        
    def parse_cat_page(self, response):
        category_name = response.meta['category_name']
        books = response.css('div.post-content-body p a::attr(href)').getall()
        books = books[1:]
        books = books[:-1]
        books = list(set(books))

        for book in books:

            book_url = 'https://allaboutethio.com/' + book

            book_name = book.split('.')[0]

            yield response.follow(book_url, callback = self.parse_book_page, meta={'category_name': category_name, 'book_name': book_name})
        
        next_pages = response.css('.page-link ::attr(href)').getall()
        next_pages = next_pages[1:]
        next_pages = next_pages[:-1]

        for next_page in next_pages:

            next_page_url = 'https://allaboutethio.com/' + next_page
            
            yield response.follow(next_page_url, callback = self.parse_cat_page, meta={'category_name': category_name})

    def parse_book_page(self, response):
        category_name = response.meta['category_name']
        book_name = response.meta['book_name']        
        pdfs = response.css('table td a::attr(href)').getall()

        for pdf in pdfs:
            
            pdf_url = 'https://allaboutethio.com/' + pdf

            pdf_name = pdf_url.split('/')[-1]

            category_dir = os.path.join('downloads', category_name)
            book_dir = os.path.join(category_dir, book_name)
            if not os.path.exists(book_dir):
                os.makedirs(book_dir)
            file_path = os.path.join(book_dir, pdf_name)
            # Download and save PDF
            urllib.request.urlretrieve(pdf_url, file_path)

        
        
        
