#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.items = []
        self.total = 0
        self.last_item_price = 0
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_item_price = price

        for n in range(quantity):
            self.items.append(title)
            self.transactions.append({"title": title, "quantity": quantity, "price": price})

        return self.items

    def apply_discount(self):
        self.total -= int(self.total * self.discount / 100)

        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.transactions[-1]["price"] * self.transactions[-1]["quantity"]

        for n in range(self.transactions[-1]["quantity"]):
            self.items.pop()

        return self.total
