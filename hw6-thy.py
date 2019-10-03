# ---------------------------------------------------------------------
# Name: Homework 6
# Purpose: Mimic activities of a fictional online store using classes
# Author: Kiwibud
# ---------------------------------------------------------------------


class Product:
    serial_number = 1
    product_id = ''
    category = 'GN'

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.sales = []
        self.reviews = []
        self.generate_product_id()

    def restock(self, quantity):
        self.stock += quantity

    def review(self, stars, text):
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        if quantity > self.stock:
            print(f'There are only {self.stock} available')
            for i in range(self.stock):
                self.sales.append(sale_price)
            self.restock(-self.stock)

        else:
            for i in range(quantity):
                self.sales.append(sale_price)
            self.restock(-quantity)

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.product_id}\n' \
               f'List price: ${self.list_price:.2f}\n' \
               f'Available in stock: {self.stock}'

    @classmethod
    def generate_product_id(cls):
        serial_num = cls.serial_number
        # update serial number - class variable
        cls.serial_number += 1
        cls.product_id = f'{cls.category}{serial_num:06}'

    @property
    def lowest_price(self):
        if len(self.sales) == 0:
            return None
        else:
            return min(self.sales)

    @property
    def average_rating(self):
        if len(self.reviews) == 0:
            return None
        else:
            return sum(stars for text, stars in self.reviews) / len(
                self.reviews)


class VideoGame(Product):
    serial_number = 1
    category = 'VG'

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):
    serial_number = 1
    category = 'BK'

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    # DO WE NEED TO CHECK IF THE SAME BOOK???
    def __lt__(self, other):
        return self.pages < other.pages

    def __eq__(self, other):
        return self.pages == other.pages


class Bundle(Product):
    serial_number = 1
    category = 'BL'

    def __init__(self, product1, product2, *products):
        description = product1.description + product2.description
        price = product1.list_price + product2.list_price
        for each_product in products:
            description += each_product.description
            price += each_product.list_price
        discount = 0.2
        price *= (1 - discount)
        super().__init__(description, price)


def main():
    print('-----------------------------------')
    print('       Testing Product class')
    print('-----------------------------------')
    sunglasses = Product("Vans Hip Cat Sunglasses", 14)
    headphones = Product("Apple Airpods", 159)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)
    print(headphones)
    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)
    print(sunglasses)
    headphones.sell(8, 140)  # There are only 5 available
    print(headphones.sales)
    print(headphones)
    sunglasses.restock(10)
    print(sunglasses)
    headphones.restock(20)
    print(headphones)
    sunglasses.review(5, "Great sunglasses! Love them.")
    sunglasses.review(3, "Glasses look good but they scratch easily")
    headphones.review(4, "Good but expensive")
    print(sunglasses.reviews)
    print(headphones.reviews)
    print(sunglasses.lowest_price)
    print(sunglasses.average_rating)
    backpack = Product("Nike Explore", 60)
    print(backpack)
    print(backpack.average_rating)
    print(backpack.lowest_price)

    print('-----------------------------------')
    print('       Testing Video class')
    print('-----------------------------------')
    mario = VideoGame('Mario Tennis Aces', 50)
    print(mario)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario.sales)
    print(mario)
    print(mario.lowest_price)
    mario.review(5, "Fun Game!")
    mario.review(3, "Too easy")
    mario.review(1, "Boring")
    print(mario.average_rating)
    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)
    lego.restock(5)
    lego.sell(10, 20)
    print(lego)
    print(lego.lowest_price)
    print('-----------------------------------')
    print('       Testing Book class')
    print('-----------------------------------')
    book1 = Book("The Quick Python Book", "Naomi Ceder", 472, 39.99)
    print(book1.author)
    print(book1.pages)
    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, "Excellent how to guide")
    print(book1)
    print(book1.average_rating)
    print(book1.lowest_price)
    book2 = Book("Learning Python", "Mark Lutz", 1648, 74.99)
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)
    print(book1 > book2)
    print(book1 < book2)
    print('-----------------------------------')
    print('       Testing Bundle class')
    print('-----------------------------------')
    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)


if __name__ == "__main__":
    main()
