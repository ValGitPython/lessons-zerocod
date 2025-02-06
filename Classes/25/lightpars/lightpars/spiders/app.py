import scrapy

class SvetilnikiSpider(scrapy.Spider):
    name = "svetilniki"
    allowed_domains = ["vselustry.ru/"]
    start_urls = ["https://vselustry.ru/catalog/svetilniki/"]

    def parse(self, response):
        # Предполагается что информация о каждом товаре находится внутри тегов div с классом product
        for product in response.css('div.product-item-container'):  # Замените 'div.product' на правильный CSS селектор
            yield {
                'name': product.css(' div.product-item-title>a::text').get(),  # Замените 'a.product-name' на правильный CSS селектор для имени товара
                'price': product.css('span.product-item-price-current::text').get().replace("\xa0", ""),     # Замените 'span.price' на правильный CSS селектор для цены
                'link': product.css('div.product-item-title>a::attr(href)').get()  # Замените 'a.product-name' на правильный CSS селектор для ссылки
            }

        # Обработка пагинации если она есть
        next_page = response.css('a.next-page-link::attr(href)').get()  # Замените 'a.next-page-link' на правильный CSS селектор для следующей страницы
        if next_page is not None:
            yield response.follow(next_page, self.parse)