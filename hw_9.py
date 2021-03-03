# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    def __get__(self, instance, owner):
        # your code here
        return instance._email

    def __set__(self, instance, value):
        # your code here
        index = value.find('@')
        if index != -1:
            if value.endswith('gmail.com', index):
                instance._email = value
            else:
                raise ValueError
        else:
            raise ValueError


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()


# my_class.email = "validemail@gmail.com"
# my_class.email = "novalidemail@dsfsd"
# print(my_class.email)
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # your code here
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


# c = MyClass()
# b = MyClass()
# assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    pass


class Data:
    number = IngegerField()


# data_row = Data()
# new_data_row = Data()
#
# data_row.number = 5
# new_data_row.number = 10
#
# assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией
# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.

# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС
import random

class Product:
    storage = {}

    def __init__(self, name, description, quantity, availability, price, category):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.availability = availability
        self.price = price
        self.category = category

    # def add_product_to_storage(self):
    #     Product.storage[self.name] = self.quantity
    #
    # def del_product_from_storage(self):
    #     del Product.storage[self.name]
    #
    # def balance_product_from_storage(self):
    #     if not self.name in Product.storage:
    #         print('This item is out of stock.')
    #     else:
    #         print(f'Balance of {self.name} on storage: {Product.storage[self.name]}')


class Storage:

    def __init__(self):
        self.store = {}

    def add_to_store(self, product):
        self.store[product.name] = {}
        self.store[product.name]['description'] = product.description
        self.store[product.name]['quantity'] = product.quantity
        self.store[product.name]['availability'] = product.availability
        self.store[product.name]['price'] = product.price
        self.store[product.name]['category'] = product.category

    def del_from_store(self, product):
        del self.store[product.name]

    def one_balance(self, product):
        if not product.name in self.store:
            print('This item is out of stock.')
        else:
            print(f'Balance of {product.name} on storage: {self.store[product.name]["quantity"]}')

    def all_balance(self):
        all_prod = {}
        # d = {self.store: self.store[product.name]['quantity'] for product in self.store}
        # print(d)
        for prod in self.store:
            # print(prod)
            for qa in self.store[prod]:
                # print(qa)
                if qa == 'quantity':
                    all_prod[prod] = self.store[prod][qa]
                    # print(f'The rest of all goods:{prod} - {self.store[prod][qa]}')
        # print(self.store)
        print(f'The rest of all goods: {all_prod}')

    def get_prod_category(self, category):
        category_list = []
        for prod in self.store:
            for cate in self.store[prod]:
                if cate == 'category' and self.store[prod][cate] == category:
                    category_list.append(prod)
        print(f'List products by category "{category}": {category_list}')


class ShoppingBasket:

    def __init__(self):
        self.basket = {}

    def add_to_basket(self, **kwargs):
        self.order_id = 1
        # if need <= product.availability:
        #     self.basket[self.order_id] = {}
        #     self.basket[self.order_id]['name'] = product.name
        #     self.basket[self.order_id]['need'] = need
        #     self.basket[self.order_id]['total_price'] = product.price * need
        #     print(f'Your order number: {self.order_id}')
        #     self.order_id += 1
        # else:
        #     print('The required quantity of goods is not in stock.')
        # self.order_id += 1

    def get_order(self, order_id):
        if order_id == self.order_id:
            print('There is no such order.')
        else:
            print(self.basket[order_id])

product_banana = Product('Banana', 'Yummy', 10, 10, 20, 'fruit')
# product_apple = Product('Apple', 'Yummy', 20, 20, 5, 'fruit')
# product_potato = Product('Potato', 'Best food', 35, 35, 15, 'vegetable')

storage = Storage()
# storage.add_to_store(product_banana)
# storage.add_to_store(product_apple)
# storage.add_to_store(product_potato)
# storage.one_balance(product_banana)
# storage.all_balance()
# storage.get_prod_category('fruit')

shopping_basket = ShoppingBasket()
shopping_basket.add_to_basket(product_banana, 2)
shopping_basket.get_order(1)