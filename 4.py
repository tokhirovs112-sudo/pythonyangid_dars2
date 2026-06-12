class Phone:
    def __init__(self, brand, model, narx, yili):
        self.brand = brand
        self.model = model
        self.narx = narx
        self.yili = yili

    def update_price(self, yangi_narx):
        self.narx = yangi_narx


telefon1 = Phone("Samsung", "S25", 1000, 2025)

print(telefon1.brand)
print(telefon1.model)
print(telefon1.narx)
print(telefon1.yili)

telefon1.update_price(900)

print("Yangi narx:", telefon1.narx)