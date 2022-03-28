f = open("egri.txt", encoding="utf-8")
lista = []
for i in f:
    i = i.strip().split(" ")
    lista.append(i)
print(f"Az Egri csillagok {len(lista)} szóból áll")
magyar = 0
torok = 0
for y in lista:
    for i in y:
        # i=i.lower()
        if i == "magyar" or i == "magyarok" or i =="Magyar" or i=="Magyarok":
            magyar += 1
        if i == "török" or i == "törökök" or i == "Törökök" or i == "Török":
            torok += 1

print(f"A török szó ennyiszer szerepel: ",torok)
print(f"A magyar szó ennyiszer szerepel",magyar)
szotar={}
for y in lista:
    for i in y:
        szotar[i]=szotar.get(i,0)+1
print(szotar)
a=(max(szotar.values()))
puska=False
db=0
for index,i in szotar.items():
    if i==a:
        print(f"A leggyakrabban szerepelt szó: {index}")
    if index=="puska":
        puska=True
        db+=1
if puska:
    print("Szerepel benne, ennyiszer: ",db)
db=0
for y in lista:
    for i in y:
        db+=1
print("Ennyi betűből áll: ",db)
lista2=[]
for i in sorted(szotar.values(),key=lambda i:i,reverse=True):
    lista2.append(i)
    if len(lista2)==10:
        break
halmaz=set()
for i in lista2:
    for index,y in szotar.items():
        if i==y:
            halmaz.add(index)
print(halmaz)


