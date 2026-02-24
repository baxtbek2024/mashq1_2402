class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def open(self):
       print("Do'kon ochildi")

class Onlineshop(Shop):
    def __init__(self, name, website, address):
        super().__init__(name, address)
        self.website = website

    def open(self):
        print("Do'kon ochildi")
        super().open()

dokon = Onlineshop("shalikxana", "shashlik.uz", "drujba")
print(dokon.name, dokon.website, dokon.address)
