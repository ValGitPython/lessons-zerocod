class Store():
    def __init__(self, name, address):

        self.name = name # название магазина.

        self.address = address # адрес магазина.

        self.items = {} # словарь, где ключ # название товара, а значение # его цена. Например, `{'apples'# 0.5, 'bananas'# 0.75}`.

# Методы класса#

#  метод для добавления товара в ассортимент.
    def add_item(self, name_product, price_product):
       self.items[name_product] = price_product 


# метод для удаления товара из ассортимента.
    def del_item(self, name_product):
       del self.items[name_product] 

# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.

# метод для обновления цены товара.
    def change_item(self, name_product, price_product):
       self.items[name_product] = price_product  


#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.

store1 = Store("Булочная","Степная 10")
store1.add_item("белый хлеб","35")
store1.add_item("багет","45")
store1.add_item("кукурузный хлеб","50")
store1.add_item("хлеб с добавками","55")

store2 = Store("Кондитерская","Ленина 47")
store2.add_item("корзинки","50")
store2.add_item("заварные","65")
store2.add_item("сладкая картошка","35")
store2.add_item("терамису","70")

store3 = Store("Продукты 1"," Маяковского 97")
store3.add_item("печенье овсяное","85")
store3.add_item("нарзан","35")
store3.add_item("пепсикола","70")

store4 = Store("Табак","Толстого 64")
store4.add_item("мальборо","120")
store4.add_item("парламент","160")
store4.add_item("махорка","25")

store5 = Store("Спортивный","Элеваторная 16")
store5.add_item("гантели 30кг","1200")
store5.add_item("гриф штанги","400")
store5.add_item("перчатки боксерские","1700")



#Выбери один из созданных магазинов и протестируй все его методы# добавь товар, обнови цену, убери товар и запрашивай цену.
price = store3.items['печенье овсяное']
print(f"цена  печенье овсяное {price}")
store3.add_item("сметана","168")
store3.change_item("печенье овсяное","105")
store3.del_item("пепсикола")
price = store3.items['печенье овсяное']
print(f"цена  печенье овсяное {price}")