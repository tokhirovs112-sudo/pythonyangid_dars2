class Avto:
    def __init__(self, nomi, rangi, narx, probegi, tezligi):
        self.nom = nomi
        self.rang = rangi
        self.narx = narx
        self.probeg = probegi
        self.tezlik = tezligi
    
    def update_probeg(self):
        n = input("Probegni o'zgartirmoqchimisiz? Ha/Yo'q: ")
        if n == "Ha":
            k = int(input("Qancha qo'shmoqchisiz?: "))
            self.probeg += k
            print("Probeg o'zgartirildi!\n Yangi probeg: ", self.probeg)
        elif n == "Yo'q":
            print("Ok")
        else:
            print("ok")
    
    def update_narx(self):
        l = input("Narxni o'zgartirmoqchimisiz? Ha/Yo'q: ")
        if l == "Ha":
            amount = int(input("Miqdorni kiriting: "))
            o = input("Tasdiqlash uchun Ha ni bosing, Otmen uchun esa Yo'q ni: ")
            if o == "Ha":
                self.narx += amount
                print("Yangi narx: ", self.narx)   
            elif o == "Yo'q":
                self.narx -= amount
                print("Yangi narx: ", self.narx)
            else:
                print("Iltimos Ha yoki Yo'q ni tanlang")
                return l

s2 = Avto("KIA", "Oq", 25000000, 20000, 200) 
s2.update_probeg()
s2.update_narx()
