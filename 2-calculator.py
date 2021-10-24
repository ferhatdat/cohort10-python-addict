print("""****************************
Hesap Makinesi Programı

İşlemler;

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme

Çıkış içim "q" tuşuna basın..

****************************""")
while True:
    işlem = input("İşlem seçiniz: ")

    if (işlem == "q"):
        print("Program Kapatılıyor")
        print("Güle güle!")
        break
    elif (işlem =="1"):
        sayı_1 = int(input("Birinci Sayı: "))
        sayı_2 = int(input("İkinci Sayı: "))
        print("{} ile {} sayısının toplamı {}'dır".format(sayı_1, sayı_2, sayı_2+sayı_1))
    elif (işlem =="2"):
        sayı_1 = int(input("Birinci Sayı: "))
        sayı_2 = int(input("İkinci Sayı: "))
        print("{} - {} : {}'dır".format(sayı_1, sayı_2, sayı_1 - sayı_2))
    elif (işlem =="3"):
        sayı_1 = int(input("Birinci Sayı: "))
        sayı_2 = int(input("İkinci Sayı: "))
        print("{} x {} : {}'dır".format(sayı_1, sayı_2, sayı_2 * sayı_1))
    elif (işlem =="4"):
        sayı_1 = int(input("Birinci Sayı: "))
        sayı_2 = int(input("İkinci Sayı: "))
        print("{} / {} : {:.2f}'dır".format(sayı_1, sayı_2, sayı_1 / sayı_2))
    else:
        print("Geçersiz İşlem")