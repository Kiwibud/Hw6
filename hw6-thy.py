# ---------------------------------------------------------------------
# Name: Homework 6
# Purpose: Mimic activities of a fictional online store using classes
# Author: Kiwibud
# ---------------------------------------------------------------------
"""
Implement classes to manipulate items sold by a fictional online store

Product class to represent the general product
VideoGame class to represent a video game
Book class to represent a book
Bundle class to represent a bundle of products
"""


class Product:
    """
    Represent a general product

    Arguments:
    description (string): product's description
    list_price (number): product's list price

    Attributes:
    description (string): product's description
    list_price (number): product's list price
    stock (number): amount of available products
    sales (list): list of actual sale prices
    reviews (list): list of user reviews
    """
    serial_number = 1
    category = 'GN'
    product_id = ''

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.sales = []
        self.reviews = []
        self.generate_product_id()

    def restock(self, quantity):
        """
        Update the amount of available products
        :param quantity: (number) quantity of products
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add reviews to list of user reviews
        :param stars: (number) rating stars
        :param text: (string) review
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Check stock and update amount of products after selling
        :param quantity: (number) requested quantity of products
        :param sale_price: (number) sale price
        :return: None
        """
        if quantity > self.stock:
            print(f'There are only {self.stock} available')
            for _ in range(self.stock):
                self.sales.append(sale_price)
            self.restock(-self.stock)

        else:
            for _ in range(quantity):
                self.sales.append(sale_price)
            self.restock(-quantity)

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.product_id}\n' \
               f'List price: ${self.list_price:.2f}\n' \
               f'Available in stock: {self.stock}'

    @classmethod
    def generate_product_id(cls):
        """
        Generate the product id
        :return: None
        """
        serial_num = cls.serial_number
        # update serial number - class variable
        cls.serial_number += 1
        cls.product_id = f'{cls.category}{serial_num:06}'

    @property
    def lowest_price(self):
        """
        Get the lowest price of the sale prices list
        :return: (number) lowest price or price
        """
        if len(self.sales) == 0:
            return None
        else:
            return min(self.sales)

    @property
    def average_rating(self):
        """
        Get the average rating stars
        :return: (number) average rating
        """
        if len(self.reviews) == 0:
            return None
        else:
            return sum(stars for (text, stars) in self.reviews) / len(
                self.reviews)

    def __add__(self, other):
        return Bundle(self, other)


class VideoGame(Product):
    """
    Represent a video game
    Inherits from: Product

    Arguments:
    description (string): product's description
    list_price (number): product's list price

    Attributes:
    description (string): product's description
    list_price (number): product's list price
    stock (number): amount of available products
    sales (list): list of actual sale prices
    reviews (list): list of user reviews

    """
    serial_number = 1
    category = 'VG'

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):
    """
    Represent a book
    Inherits from: Product

    Arguments:
    description (string): product's description
    list_price (number): product's list price

    Attributes:
    description (string): product's description
    list_price (number): product's list price
    stock (number): amount of available products
    sales (list): list of actual sale prices
    reviews (list): list of user reviews
    author (string): author's name
    pages (number): number of pages

    """
    serial_number = 1
    category = 'BK'

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    def __lt__(self, other):
        return self.pages < other.pages

    def __eq__(self, other):
        return self.pages == other.pages


class Bundle(Product):
    """
    Represent a bundle of two or more products
    Inherits from: Product

    Arguments:
    first (Product): first product
    second (Product): second product
    args (Product): 0 or more products

    Attributes:
    description (string): product's description
    list_price (number): product's list price
    stock (number): amount of available products
    sales (list): list of actual sale prices
    reviews (list): list of user reviews

    """
    serial_number = 1
    category = 'BL'
    bundle_discount = 0.8

    def __init__(self, first, second, *args):
        self.description = f'{first.description} & {second.description}'
        self.list_price = first.list_price + second.list_price
        for arg in args:
            self.description += f' & {arg.description}'
            self.list_price += arg.list_price
        self.list_price *= self.bundle_discount
        super().__init__(self.description, self.list_price)

    """
    The corresponding to the best_bundle is BL000006. 
    Every time we add 2 products,we create a Bundle object,
    which will increment the variable serial_number by 1. 
    -The serial_number starts from BL000003 (back_to_school_bundle) 
    b1 = sunglasses + headphones=> BL000004
    b2 = b1 + book1 		    => BL000005
    best_bundle = b2 + mario	=> BL000006
    """


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
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(2, 95)
    print(bundle1)
    print(bundle1.lowest_price)
    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)
    best_bundle = sunglasses + headphones + book1 + mario
    print(best_bundle)


if __name__ == "__main__":
    main()
