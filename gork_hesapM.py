def add (a,b):
  print(a+b)
def sub(a,b):
  print(a-b)
def mul(a,b):
  print(a*b)
def div(a,b):
  print(a/b)

while True:
  grk = int(input("1- Toplama, 2- Çıkarma, 3- Çarpma, 4- Bölme, 5- Çıkış: "))
  if grk== 5:
      break
  if grk>5:
    print("geçersiz giriş")
    break
  try:
    a = int(input("sayı 1: "))
    b = int(input("sayı 2: "))
  except:
      print("geçerli sayı girin")
      continue
    
  if grk== 1:
      add(a, b)
  elif grk== 2:
      sub(a, b)
  elif grk== 3:
      mul(a, b)
  elif grk== 4:
      div(a, b)
  else:
      print("geçersiz giriş.")



