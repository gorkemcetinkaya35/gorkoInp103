sinav1 = int(input("1. Sınav notunu giriniz"))
sinav2 = int(input("2.Sınav notunu giriniz"))
istenenOrtalama = int(input("İstediğiniz ortalama nedir"))

ort = istenenOrtalama*3
gerekenNot = ort - (sinav1 + sinav2)
print("Gereken not: " + str(gerekenNot))
