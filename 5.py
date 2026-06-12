class Employee:
    def __init__(self, ism, familiya, ish_sanasi, lavozim, maosh):
        self.ism = ism
        self.familiya = familiya
        self.ish_sanasi = ish_sanasi
        self.lavozim = lavozim
        self.maosh = maosh
        self.bonus = 0

    def set_bonus(self):
        if self.maosh < 10_000_000:
            self.bonus = self.maosh * 25 / 100


hodim1 = Employee("Ali", "Karimov", "2025-01-10", "Dasturchi", 8_000_000)

hodim1.set_bonus()

print("Ism:", hodim1.ism)
print("Lavozim:", hodim1.lavozim)
print("Maosh:", hodim1.maosh)
print("Bonus:", hodim1.bonus)