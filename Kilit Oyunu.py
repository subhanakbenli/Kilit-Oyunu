# # Kilit Oyunu Projesi
import time # kapanma efekti için eklendi 
def KilitOyunu():
    # Oyunculardan bilgiler alınıyor

    BirinciOyuncu=input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
    IkinciOyuncu=input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
    while True:# oyun alanının büyüklüğünü kullanıcıdan alıp doğruluğunu kontrol eden döngü
        try:
            SatirSutun=int(input("Oyun alanının satır sütun sayısını giriniz(4-8):"))
        except:
            print("! lütfen sayı girişi yapınız")
            continue
        if 9>SatirSutun>3:
            break
        else:
            print("satır sütun sayısı 4-8 aralığındadır")
    
    # Alınan bilgilere uygun olarak Sözlük yapısı oluşturuluyor
    listeSutun=["A","B","C","D","E","F","G","H"]
    listeSutun=listeSutun[0:SatirSutun]
    TabloSozlugu={}
    for satir in range(1,SatirSutun+1):
        for sutun in listeSutun:
            if satir==1:
                TabloSozlugu[f"{satir}{sutun}"]=f" {BirinciOyuncu} "
            elif satir==SatirSutun:
                TabloSozlugu[f"{satir}{sutun}"]=f" {IkinciOyuncu} "
            else:
                TabloSozlugu[f"{satir}{sutun}"]="   "
    sayac=1
    
    while True: # oyuncuların hamle yapacağı ve her hamleden sonra kontrol edecek döngü
        EkranaYazdır(SatirSutun,listeSutun,TabloSozlugu)
        if sayac%2!=0: # sıranın hangi oyuncuda olduğunu sorgulayan koşul
            oyuncu=BirinciOyuncu
            rakipOyuncu=IkinciOyuncu
        else:
            oyuncu=IkinciOyuncu
            rakipOyuncu=BirinciOyuncu
        
        hamle=input(f"Oyuncu {oyuncu},lütfen hareket ettirmek istediğiniz taşınızın konumunu ve hedef konumu giriniz")
        HamleKordinatlari=hamle.upper().split(" ")
        
        if len(HamleKordinatlari)!=2 :# girilen verinin doğru formatda girilmesini sorgulayan koşul
            print("! Hamle kordinatlarını aralarında bir boşluk olacak şekilde yazınız.Örnek:'A1 B2'")
            continue
        elif len(HamleKordinatlari[0])!=2 :
            print("Hamle kordinatlarının formatını kontrol ediniz")
            continue
        elif len(HamleKordinatlari[1])!=2 :
            print("Hamle kordinatlarının formatını kontrol ediniz")
            continue
        if HamleKordinatlari[0]==HamleKordinatlari[1]:# aynı konuma tekrar oynanıp oynanmadığını kontrol eder
            print("! Hamle kordinatları aynı girildi lütfen tekrar deneyiniz.")
            continue
        EskiYer=HamleKordinatlari[0]
        YeniYer=HamleKordinatlari[1]
        try:
            deger=str(TabloSozlugu[EskiYer]).strip()
            deger2=str(TabloSozlugu[YeniYer]).strip()
        except:
            print("Hamle kordinatlarının formatını kontrol ediniz")
            continue
        if deger==oyuncu: # girilen kordinatda oyuncunun taşı olup olmadığını kontrol eder 
            if EskiYer[1]==YeniYer[1]:# Oyuncunun dikeyde hareket yönünü kontrol eder
                
                KontrolDegeri=0
                if EskiYer[0]>YeniYer[0]:
                    rangeListe=range(int(YeniYer[0]),int(EskiYer[0]))
                elif EskiYer[0]<YeniYer[0]:
                    rangeListe=range(int(EskiYer[0])+1,int(YeniYer[0])+1)
                for satir in rangeListe: # taşın gideceği yönde farklı bir taş olup olmadığını kontrol eder
                    hucre=TabloSozlugu[f"{satir}{EskiYer[1]}"]
                    if hucre!="   ":
                        KontrolDegeri=1
                        break

                if KontrolDegeri==1:
                    print("! Bu konuma hareket edemezsiniz lütfen tekrar deneyiniz")
                    continue
            elif EskiYer[0]==YeniYer[0]:# Oyuncunun yatayda hareket  yönünü kontrol eder
                Yer1Index=listeSutun.index(str(EskiYer[1]))# listeden Sütunların indexlerinini alır 
                Yer2Index=listeSutun.index(YeniYer[1])
                KontrolDegeri=0
                if Yer1Index>Yer2Index:# İndexlerin büyüklüğünü sorgular
                    KontrolListesi=listeSutun[Yer2Index:Yer1Index]
                elif Yer2Index>Yer1Index:
                    KontrolListesi=listeSutun[Yer1Index+1:Yer2Index+1]

                for sutun in KontrolListesi: # taşın gideceği yönde farklı bir taş olup olmadığını kontrol eder
                    hucre=TabloSozlugu[f"{EskiYer[0]}{sutun}"]
                    if hucre!="   ":
                        KontrolDegeri=1
                        break
                
                if KontrolDegeri==1: 
                    print("! Bu konuma hareket edemezsiniz lütfen tekrar deneyiniz")
                    continue
            else:
                print("! Taşlarınızı sadece yatay ve dikeyde hareket ettirebilirsiniz.")
                continue
            TabloSozlugu[EskiYer]="   "
            try:
                TabloSozlugu[YeniYer]=f" {oyuncu} "
            except:
                print("Hamle kordinatlarının formatını kontrol ediniz")
                continue
            sayac+=1
            
            for satir in range(1,SatirSutun+1): # oyun alanındaki taşları kontrol edip çıkartılacak taşları silecek döngü
                for sutun in listeSutun:
                    
                    veri=TabloSozlugu[f"{satir}{sutun}"]
                    if str(veri) == " "+rakipOyuncu+" ": # Rakip oyuncunun taşlarının etrafında iki tane taş olup olmadığını kontrol eder
                        if 1<satir<SatirSutun: # orta satırlar
                            sutunIndex=listeSutun.index(sutun)
                            
                            if 0<sutunIndex<SatirSutun-1:# orta sütunlar
                                xx=satir-1
                                komsu1=TabloSozlugu[f"{xx}{sutun}"]
                                xx=satir+1
                                komsu2=TabloSozlugu[f"{xx}{sutun}"]
                                komsu3=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex-1])]
                                komsu4=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex+1])]
                                
                                liste=[komsu1,komsu2]
                                liste2=[komsu3,komsu4]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                rakipSayisi2=liste2.count(f" {oyuncu} ")
                                
                                if rakipSayisi>=2 or rakipSayisi2>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==0:# ilk sütun
                                xx=satir-1
                                komsu1=TabloSozlugu[f"{xx}{sutun}"]
                                xx=satir+1
                                komsu2=TabloSozlugu[f"{xx}{sutun}"]
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==SatirSutun-1:# son sütun
                                xx=satir-1
                                komsu1=TabloSozlugu[f"{xx}{sutun}"]
                                xx=satir+1
                                komsu2=TabloSozlugu[f"{xx}{sutun}"]
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                                pass

                        elif satir==1:# ilk satır
                            sutunIndex=listeSutun.index(sutun)
                            
                            if 0<sutunIndex<SatirSutun-1: # orta sütunlar
                                xx=satir+1
                                komsu1=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex-1])]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex+1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==0:# ilk sütun 
                                
                                komsu1=TabloSozlugu[f"{2}{sutun}"]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex+1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==SatirSutun-1: # son sütun
                                komsu1=TabloSozlugu[f"{2}{sutun}"]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex-1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass

                        elif satir==SatirSutun:# son satır
                            sutunIndex=listeSutun.index(sutun)
                            
                            if 0<sutunIndex<SatirSutun-1:# orta sütunlar
                                
                                komsu1=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex-1])]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex+1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==0:# ilk sütun
                                xx=satir-1
                                komsu1=TabloSozlugu[f"{xx}{sutun}"]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex+1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                            elif sutunIndex==SatirSutun-1:# son sütun
                                xx=satir-1
                                komsu1=TabloSozlugu[f"{xx}{sutun}"]
                                komsu2=TabloSozlugu["{}{}".format(satir,listeSutun[sutunIndex-1])]
                                
                                liste=[komsu1,komsu2]
                                rakipSayisi=liste.count(f" {oyuncu} ")
                                if rakipSayisi>=2:
                                    print(f"{satir}{sutun} konumundaki taş kilitlendi.")
                                    TabloSozlugu[f"{satir}{sutun}"]="   "
                                else:pass
                    
                    else:pass
        else:print("! Lütfen girilen konumları kontrol ediniz")
        TasSay1=0
        TasSay2=0
        for satir in range(1,SatirSutun+1):
            for sutun in listeSutun:
                if TabloSozlugu[f"{satir}{sutun}"]==f" {BirinciOyuncu} ":
                    TasSay1+=1
                elif TabloSozlugu[f"{satir}{sutun}"]==f" {IkinciOyuncu} ":
                    TasSay2+=1
        if TasSay1<2:
            EkranaYazdır(SatirSutun,listeSutun,TabloSozlugu)
            print(f"Oyuncu {IkinciOyuncu} kazandı.")

            break
        if TasSay2<2:
            EkranaYazdır(SatirSutun,listeSutun,TabloSozlugu)
            print(f"Oyuncu {BirinciOyuncu} kazandı.")
            break
                    


def EkranaYazdır(SatirSutun,listeSutun,TabloSozlugu):# oluşturulan sözlük yapısı ekrana çıktı vermek için kullanılıyor
        SatirCizgisi="  -"+"----"*SatirSutun
        UstBaslik="    "+"   ".join(listeSutun)+"  "
        print(UstBaslik)        
        print(SatirCizgisi)

        for satir in range(1,SatirSutun+1):# her satırı teker teker sözlükten aldığı verilere göre dolduracak döngü
            SatirText=f"{satir} |"
            for sutun in listeSutun:
                hucre=TabloSozlugu[f"{satir}{sutun}"]
                SatirText+=hucre+"|"
            SatirText+=f" {satir}"
            print(SatirText)
            print(SatirCizgisi)
        UstBaslik="    "+"   ".join(listeSutun)+"  "
        print(UstBaslik)  
KilitOyunu()
while True:
    girdi=input("Tekrar oynamak ister misiniz?(E/H)").upper()
    if girdi=="E":
        KilitOyunu()
        
        continue
    elif girdi=="H":
        print("Oyundan çıkılıyor")
        time.sleep(0.7)
        
    else:
        print("! Lütfen tekrar cevaplayınız.")

    