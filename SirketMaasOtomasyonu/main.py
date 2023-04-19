class Sirket():
    def __init__(self, ad):
        self.ad=ad
        self.calisma=True

    def program(self):
        secim=self.Menu()

        if secim==1:
            self.CalisanEkle()

        elif secim==2:
            self.CalisanSil()

        elif secim==3:
            AYSecim=input ("Yıllık bazda görmek ister misiniz?(E/H)")
            if AYSecim=="E":
                self.VerilecekMaasGoster(hesap="Y")
            else:
                self.VerilecekMaasGoster()

        elif secim==4:
            self.MaaslariVer()


    def Menu(self):
        secim=int(input("---{} Otomasyonuna Hosgeldiniz---\n\n1-Çalışan Ekle\n2-Çalışan Çıkart\n3-Verilecek Maaş Göster\n4-Maaşları Ver\nSeçiminizi Giriniz: ".format(self.ad)))
        
        #girilen deger kontrol
        while secim < 1 or secim >= 4:
            secim=int(input("Lütfen Belirtilen Degerler Dısında Deger Girmeyiniz: "))

        return secim
    

    def CalisanEkle(self):
        ad = input("Calısan Adı Giriniz : ")
        soyad = input("Calısan Soyadını Giriniz : ")
        yas = input("Calısan Yaşı Giriniz : ")
        cinsiyet = input("Calısan Cinsiyeti Giriniz : ")
        maas = input("Calısan Maaşı Giriniz : ")

        with open("calisanlar.txt","r",encoding="utf-8") as Dosya:
            calisanListesi = Dosya.readlines()

        if len(calisanListesi)==0:
            id=1
        else:
            with open("calisanlar.txt","r",encoding="utf-8") as Dosya:
                id=int(Dosya.readlines()[-1].split(")")[0])+1

        with open("calisanlar.txt","+a",encoding="utf-8") as Dosya:
            Dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad.upper(),soyad.upper(),yas,cinsiyet.upper(),maas))

    def CalisanSil(self):
        with open("calisanlar.txt","r",encoding="utf-8") as Dosya:
            calisanlar=Dosya.readlines()

        gCalisanlar=[]

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gCalisanlar:
            print(calisan)

        secim=int(input("Cıkartmak İstediginiz Calisanın Numarasını Giriniz(1-{}: ".format(len(gCalisanlar))))
        while secim < 1 or secim > len(gCalisanlar):
            secim=int(input("Lütfen (1-{}) Arasında Numara Giriniz: ".format(len(gCalisanlar))))

        calisanlar.pop(secim-1)

        sayac=1
        dCalisanlar=[]

        for calisan in calisanlar:
            dCalisanlar.append(str(sayac)+ ")" + calisan.split(")")[1]) 
            sayac+=1
        
        with open("calisanlar.txt","w",encoding="utf-8") as Dosya:
            Dosya.writelines(dCalisanlar)

    def VerilecekMaasGoster(self,hesap="a"):
        """hesap : a ise aylık, y ise yıllık"""

        with open("calisanlar.txt","r",encoding="utf-8") as Dosya:
            calisanlar=Dosya.readlines()

        maaslar=[]

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        if hesap =="E":
            print("Bu AY verilmesi gereken toplam maas: {} TL".format(sum(maaslar)))
        else:
            print("Bu YIL verilmesi gereken toplam maas: {} TL".format(sum(maaslar)*12))

    def MaaslariVer(self):
        with open("calisanlar.txt","r",encoding="utf-8") as Dosya:
            calisanlar=Dosya.readlines()

        maaslar=[]

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplamMaas=sum(maaslar)

        #bütceden veriyi almak icin
        with open("butce.txt","r",encoding="utf-8") as Dosya:
            tButce=int(Dosya.readlines()[0])

        tButce= tButce - toplamMaas

        with open("butce.txt","w",encoding="utf-8") as Dosya:
            Dosya.write(str(tButce))


sirket=Sirket("X Bilisim")
while sirket.calisma:
    sirket.program()