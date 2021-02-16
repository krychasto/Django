class dodawanie():

    def __init__(self):
        print("Utworzono dodawanie")

    def dodaj(self,x,b):
        return x+b

class kalkulator(dodawanie):

    def odejmowanie(self,x,b):
        return x-b


kalk = kalkulator()
print(kalk.odejmowanie(4,5))
print(kalk.dodaj(4,5))
