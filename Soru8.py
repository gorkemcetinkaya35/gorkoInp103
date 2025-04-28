lst = []
ciftlist = []

while True:
    a = input("Listeye eklenecek sayıları girin, çıkmak için 'cikis' yazın: ")
    
    if a != "cikis":
        try:
            a = float(a)
        except:
            print("Lütfen geçerli bir sayı girin.")
            continue
        
        lst.append(a)
        
        if a % 2 == 0:
            ciftlist.append(a)
    else:
        break

print("Çift sayılar:", ciftlist)
