import random
#ex2


invalid=True
while invalid:
    nota=float(input("introdu nota: "))
    if nota<5:
        print("reexaminare")
        invalid=False
    elif nota >=5 and nota<=6:
        print("suficient")
        invalid=False
    elif nota >=7 and nota <=8:
        print("bine")
        invalid=False
    elif nota >=9 and nota <=10:
        print("excelent")
        invalid=False
    else:   
        print("nota invalida")    

#ex3

start_interval=int(input("introduceti capatul inferior al intervalului: "))
stop_interval=int(input("introduceti capatul superior al intervalului: "))

secret_number=random.randint(start_interval,stop_interval)
number=int(input("ghiceste numarul: "))
ghicit=False
while ghicit==False:
    if number==secret_number:
        print("ai ghicit numarul")
        ghicit=True
    elif number<secret_number:
        print("numarul este mai mare")
    else:    print("numarul este mai mic")
    number=int(input("ghiceste numarul: "))

#ex4

list=["bucuresti","sibiu","cluj","timisoara","iasi","constanta"]

enumerated_list=enumerate(list, start=1)
for index, element in enumerated_list:
    print(f"{index}. {element}")

#ex5

list=[]

for i in range(6):
    number=int(input(f"introduceti numarul {i+1}: "))
    list.append(number)
print(list)

rnd_list=[]
for i in range(6):
    rnd_list.append(random.randint(1,49))
print("numere extrase:", rnd_list)

numare_ghicite=[]
for number in list:
    if number in rnd_list:
        numare_ghicite.append(number)
print("numere ghicite:", numare_ghicite)

#ex7

comentariu=input("introduceti un comentariu: ")
comentariu_separat=comentariu.split()

lista_cuvinte_bune=["bine", "frumos", "super", "excelent", "minunat"]
lista_cuvinte_rele=["urât", "prost", "groaznic", "dezamăgitor"]

ct_bun=0
ct_rau=0

for cuvant in comentariu_separat:
    if cuvant in lista_cuvinte_bune:
        ct_bun+=1
    elif cuvant in lista_cuvinte_rele:
        ct_rau+=1
if ct_bun>ct_rau:
    print("comentariu pozitiv")
elif ct_rau>ct_bun:
    print("comentariu negativ")
else:
    print("comentariu neutru")

#ex8


while True:
        print("introdu detaliile tranzactiei:")
        suma=int(input("suma:"))
        tara=input("tara: ")
        tari_cu_risc=["Coreea de Nord", "Siria", "Iran"]
        prag_suma_risc=10000
        numar_tranzactii_risc_maxim=3
        numar_tranzactii_risc=0
        if tara in tari_cu_risc:
            numar_tranzactii_risc+=1
            print("tranzactie suspecta detectata")
        if suma>prag_suma_risc:
            numar_tranzactii_risc+=1
            print("tranzactie suspecta detectata")
        if numar_tranzactii_risc>=numar_tranzactii_risc_maxim:
            print("tranzactie suspecta detectata")
            break