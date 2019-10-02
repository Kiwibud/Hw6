# ---------------------------------------------------------------------
# Name: Homework 6
# Purpose: Mimic activities of a fictional online store using classes
# Author: Kiwibud
# ---------------------------------------------------------------------


class Product:
    serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.category = 'GN'
        self.id = self.generate_product_id(self.category)
        self.sales = []
        self.reviews = []

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
            # print(f'{self.stock} Stock')

        else:
            for i in range(quantity):
                self.sales.append(sale_price)
            self.restock(-quantity)
            # print(f'{self.stock} Stock')

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.id}\n' \
               f'List price: ${self.list_price:.2f}\n' \
               f'Available in stock: {self.stock}'

    @classmethod
    def generate_product_id(cls, category):
        serial_num = cls.serial_number
        # update serial number - class variable
        cls.serial_number += 1
        return f'{category}{serial_num:06}'

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

    def __init__(self, description, list_price):
        self.category = 'VG'
        super().__init__(description, list_price)


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


if __name__ == "__main__":
    main()
