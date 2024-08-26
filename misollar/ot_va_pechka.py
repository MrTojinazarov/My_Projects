def ot_va_pechka(ot, pechka):
    
    x1 = int(ot[0])
    y1 = (ord(ot[1]))-64

    x = int(pechka[0])
    y = ord(pechka[1])-64

    if x1 < 1 or x < 0 or 8 < x1 or 8 < x or y1 < 1 or y < 0 or 8 < y1 or 8 < y:
        print("Shaxmat doskasida bunday katak yo'q")
        return

    if (abs(x1-x) == 2 and abs(y1-y) == 1) or (abs(y1-y) == 2 and abs(x1-x) == 1):
        print("Yes")
    else:
        print("No")


ot = input("Ot = ")
pechka = input("Pechka = ")

ot_va_pechka(ot, pechka)