

class Kawa():
    def __init__(self,nazwa,woda,mleko,cukier,kawa,cena):
        self.nazwa = nazwa
        self.woda = woda
        self.mleko = mleko
        self.cukier = cukier
        self.cena = cena
        self.kawa = kawa
        
        
        
class Kawomat():
    def __init__(self, kawy,woda,mleko,cukier,kawa, kubeczki):
        self.kawy = kawy
        self.woda = woda
        self.mleko = mleko
        self.cukier = cukier
        self.kawa = kawa
        self.kubeczki = kubeczki
        self.wrzucone = 0
        self.zarobione = 0
        
    def odejmij_zasoby(self,Kawa):
        if (self.woda - Kawa.woda) < 0 or (self.cukier - Kawa.cukier) <0 or (self.kawa - Kawa.kawa) <0 or (self.kubeczki - 1) < 0 or (self.mleko - Kawa.mleko) < 0:
            print("Not enough ingredients. Try different coffee.")
            return "za mało"
        else:    
            self.woda -= Kawa.woda
            self.cukier -= Kawa.cukier
            self.kawa -= Kawa.kawa
            self.kubeczki -= 1
            self.mleko -= Kawa.mleko
            
    def pokaz_zasoby(self):
        print("Coffee Machine: Water %d. Sugar %d. Coffee %d. Milk %d." % (self.woda,self.cukier,self.kawa, self.mleko))
        print()
        
    def przyjmij_pieniadze(self,pieniadze,Kawa,money):
        cena = Kawa.cena
        
        if money not in pieniadze:
            print("Wrong banknote.")
            print()
            return "again"
        else:
            self.wrzucone += money
        
        if self.wrzucone < cena:
            
            print("You need: %.2f PLN." % (int(cena) - int(self.wrzucone)))
            print()
            return "again"
        
        elif self.wrzucone == cena:
            print("Thank you :)")
            print()
            self.zarobione += cena
            return "ok"
        
        elif self.wrzucone > cena:
            print("Change: %.2f PLN." % (int(self.wrzucone) - int(cena)))
            print("Thank you :)")
            print()
            self.zarobione += cena
            return "ok"
        
        
def pokaz_kawy(kawy):
    przerwa = 15
    wciecie =0
    print("%Coffee Machine" % (" " * (int(przerwa/2)) ))  
    print("%s" % ("-" * (przerwa+8)))
    print("Coffee%s| Price |" % (" " * (przerwa - 4)))
    print("%s" % ("-" * (przerwa+8)))
      
    for kawa in kawy:
        nazwa = kawa.nazwa
        
        if len(nazwa) > przerwa:
            nazwa =nazwa[:przerwa-2]
            wciecie =3
        else:
            wciecie = przerwa -len(kawa.nazwa)+1
        
        print("%s%s%.2f" % (nazwa," " * wciecie, kawa.cena))

    print("%s" % ("-" * (przerwa+8)))  
    
      

kawy = [Kawa("Americano",200,0,2,100,5),Kawa("Caffe Latte",300,100,2,50,7),Kawa("Cappucino",100,50,1,50,6)]  

kawomat = Kawomat(kawy, 1000,1000,10,200,15)
pieniadze = [1,2,5,10,20]
pokaz_kawy(kawy)
kawomat.pokaz_zasoby()

odp =""
while odp != "n":
    ok=""
    while ok != "tak":
        ok=""
        try:
            kawomat.wrzucone = 0
            kawa = kawy[int(input("Choose coffee (1 - %d): " % (len(kawy)))) -1]
        except:
            print("Enter correct number")
            ok = "nie"
        finally:
            if ok != "nie":
                break
    if kawomat.odejmij_zasoby(kawa) == "za mało":
        #odp = "n"
        continue
    
    
   
    kawomat.pokaz_zasoby()
        #odp = input("Wybrałeś kawę %s. Kontynuować? (t/n)" % (kawa.nazwa))
        
        
    print("You have chosen %s. Price: %.2f PLN." % (kawa.nazwa,kawa.cena))
    dalej=""
    while dalej!= "tak" :
        money = input("Coffee Machine accepts %s :" % (pieniadze))
        if kawomat.przyjmij_pieniadze(pieniadze, kawa, int(money)) == "again":
            dalej = "nie"
            continue
        else:
            dalej = "tak"
            break
        
        
        
        
        
        
