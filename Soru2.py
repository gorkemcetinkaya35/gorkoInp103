import math

x1 = float(input("Birinci noktanın x koordinatını girin: "))
y1 = float(input("Birinci noktanın y koordinatını girin: "))
x2 = float(input("İkinci noktanın x koordinatını girin: "))
y2 = float(input("İkinci noktanın y koordinatını girin: "))
P1 = (x1, y1)
P2 = (x2, y2)

mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"İki nokta arasındaki mesafe: {mesafe}")
