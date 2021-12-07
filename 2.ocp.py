"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        print('...')


class Lion(Animal):
    def make_sound(self):
        print('roar')


class Mouse(Animal):
    def make_sound(self):
        print('squeak')


animals = [
    Lion('lion'),
    Mouse('mouse')
]


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""


class Discount:  # desconto para fav
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2


class Vip(Discount):
    def give_discount(self):
        return super().give_discount() * 2
