import random
print("Şanslı Sayı'ya Hoşgeldiniz")
input("*****Başlamak için ENTER'a basınız*****")

print("-"*30)
print("Şans Oyunu       Kod")
print("-"*15)

print("Sayısal Loto:     1")
print("Super Loto:       2")
print("On Numara:        3")
print("Sans Topu:        4")

print("-"*30)

name = input("Adınız: ")
cevap = input("Lütfen oynamak istediğiniz şans oyununun kodunu giriniz: ")

listeSay = range(1,49)
listeSup = range(1,54)
listeOn =  range(1,80)
listeSans1 = range(1,34)
listeSans2 = range(1,14)

if cevap == "1":
    sayi1 = random.sample(listeSay, 6)
    sayi1.sort(reverse=False)
    print(f"Sayın {name}, şanslı sayılarınız: {sayi1}")
elif cevap == "2":
    sayi2 = random.sample(listeSay, 6)
    sayi2.sort(reverse=False)
    print(f"Sayın {name}, şanlı sayılarınız: {sayi2}")
elif cevap == "3":
    sayi3 = random.sample(listeOn, 10)
    sayi3.sort(reverse=False)
    print(f"Sayın {name}, şanslı sayılarınız: {sayi3}")
elif cevap == "4": 
    sayi4 = random.sample(listeSans1, 5)
    sayi4.sort(reverse=False)
    sayi5 = random.sample(listeSans2, 1)
    sayi5.sort(reverse=False)
    print(f"Sayın {name}, şanslı sayılarınız {sayi4} + {sayi5} " )
else:
    print("Lütfen oynamak istediğiniz oyunun kodunu giriniz!")
print("İyi Şanslar!!")
input("*****Çıkmak için ENTER'a basınız*****")



# def sayLo(başlangıç=1, bitiş=49, adet=6):
#     sayilar = set()
#     while len(sayilar) < adet:
#         sayilar.add(random.randrange(başlangıç, bitiş))

    # return sayilar
    # print("Şanslı sayınız: {sayilar}")
