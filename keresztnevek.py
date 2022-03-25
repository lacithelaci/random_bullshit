def Hangrend(a):
    magas = "eéiíöőüű"
    mély = "aáoóuú"
    mag = False
    mely = False
    for i in magas:
        if a.__contains__(i):
            mag = True
    for i in mély:
        if a.__contains__(i):
            mely = True
    if mag and mely:
        return f"Vegyes"
    if mag == False and mely:
        return f"Mély"
    if mag and mely == False:
        return f"Magas"
    else:
        return f"Egyik sem"


def mgh(a):
    az = False
    betu = "eéiíöőüűaáoóuú"
    for i in betu:
        if a[0].__contains__(i):
            az = True
    return az


def fa(a):
    a = a.lower()
    a = a.replace("a", "afa")
    a = a.replace("o", "ofo")
    a = a.replace("u", "ufu")
    a = a.replace("e", "efe")
    a = a.replace("i", "ifi")
    a = a.replace("é", "éfé")
    a = a.replace("í", "ífí")
    a = a.replace("ö", "öfö")
    a = a.replace("ő", "őfő")
    a = a.replace("ü", "üfü")
    a = a.replace("ű", "űfű")
    a = a.replace("á", "áfá")
    a = a.replace("ó", "ófó")
    a = a.replace("ú", "úfú")
    return a
def hossz(a):
    return len(a)

f = open("Ecsegi.txt", encoding="UTF-8")
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
a = open("Vegyes.txt", "w", encoding="UTF-8")
b = open("Magas.txt", "w", encoding="UTF-8")
c = open("Mély.txt", "w", encoding="UTF-8")
for i in lista:
    if Hangrend(i.lower()) == "Vegyes":
        a.write(f"{i}\n")
    if Hangrend(i.lower()) == "Magas":
        b.write(f"{i}\n")
    if Hangrend(i.lower()) == "Mély":
        c.write(f"{i}\n")
mgh1 = 0
msh1 = 0
for i in lista:
    if mgh(i.lower()):
        mgh1 += 1
    else:
        msh1 += 1
print("Magánhangzóval kezdődő:", mgh1)
print("Mássalhangzóval kezdődő:", msh1)
random = open("fa.txt", "w", encoding="UTF-8")
for i in lista:
    random.write(f"{fa(i)}\n")
a = lista[0]
b = lista[0]
for i in lista:
    if len(a) < len(i):
        a = i
    if len(b) > len(i):
        b = i
print("Leghosszabb szó:", a)
print("Legrövidebb szó:", b)
print("ABC sorrend: ")
for i in sorted(lista):
    print(i)
print("Hossz szerint: ")
for i in sorted(lista,key=lambda i:hossz(i)):
    print(i)