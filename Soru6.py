lst=[]
while True:
    a= input("listeye eklenecek sayıları girin, çıkmak için cikis yazın")
    if a!= "cikis":
        try:
            a=float(a)
        except:
            print("listeye eklenecek sayıyı girin")
            continue
        lst.append(a)
    else:
        break
b=0
for i in lst:
    b=b+i
print(b)
