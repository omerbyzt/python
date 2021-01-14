class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesap_bilgileri(self):
        print("Isim : " ,self.isim)
        print("Numara : ",self.numara)
        print("Bakiye : ",self.bakiye)

    def para_cek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Daha yoluna yoluna yürüyemiyorsun")
        else:
            self.bakiye -= miktar
            print("Yeni bakiye = ",self.bakiye)

    def para_yatır(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiye = ",self.bakiye)

account = Account("omer",1,100)

account.hesap_bilgileri()
account.para_cek(150)
account.para_yatır(2000)

