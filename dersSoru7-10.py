#SORU 7
sozcuk=input("Bir sozcuk yazınız")
for harf in sozcuk:
    print(harf+"!")


#SORU 8 
sozcuk= input("Bir kelime yazınız")
harf= input("Bir harf yazınız")
sayma=0

for x in sozcuk:
    if x == harf:
        sayma+=1
print(sayma)        

#SORU 9
metin=input("Bir metin giriniz")
sozcuk=input("Silinecek bir sözcük giriniz")
print(metin.replace(sozcuk,""))

#SORU 10
sozcuk=input("Bir kelime giriniz")
sesli="aeıioöuü"
sayma=0
for karakter in sozcuk:
    for say in sesli:
        if say== karakter:
            sayma+=1
print(sayma)
