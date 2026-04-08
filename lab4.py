import functools
from getpass import getpass

# lis=[1, 3, 5, 6, 2]

# print("The sum of the list elements is: ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))

# print("The maximum element in the list is:",end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))


# pj=getpass("Primul jucator a ales: ")
# dj=getpass("Al doilea jucator a ales: ")

# game=True
# while game==True:
#     if pj==dj:
#         print("Remiza")
#     elif pj=="piatra" and dj=="foarfeca":
#         print("Primul jucator a castigat")
#     elif pj=="foarfeca" and dj=="hartie":
#         print("Primul jucator a castigat")
#     elif pj=="hartie" and dj=="piatra":
#         print("Primul jucator a castigat")
#     else:
#         print("Al doilea jucator a castigat")
#     continua=input("Continui jocul? y/n")
#     if continua=="n":
#         game=False


# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# n=int(input("introduceti un numar: "))
# print("fibonacci:", fibonacci(n))


# def genereaza_factura(args, **kwargs):
#     print("Clientul "+args+" a cumparat:")
#     for produs, pret in kwargs.items():
#         print("produs: "+produs+", pret: "+str(pret)+" lei")


# nume_client="Ion"
# produse={"laptop": 1500, "aspirator": 800, "mixer": 400}
# genereaza_factura(nume_client, **produse)

# def normalizare(numere):
#     numere_normalizate=[]
#     for i in numere:
#         numere_normalizate.append(1/i)
#     return numere_normalizate

# numere=[1, 2, 3, 4, 5]
# print("numere normalizate:", normalizare(numere))


# result = map(lambda x: x**2, numere)
# print("numere patrate:", list(result))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_a = sorted(a, key=lambda x: x[1])
print("lista sortata:", sorted_a)

orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pare = list(filter(lambda x: x % 2 == 0, orig_list))
print("numere pare:", lista_pare)
lista_impare=list(filter(lambda x: x % 2 != 0, orig_list))
print("numere impare:", lista_impare)

preturi={"laptop": 1500, "aspirator": 800, "mixer": None, "televizor": 2000}
preturi_filtrate=list(filter(lambda x: x[1] is not None, preturi.items()))
print("preturi filtrate:", preturi_filtrate)
preturi_reduse=list(map(lambda x: (x[0], x[1]*0.9), preturi_filtrate))
print("preturi reduse:", preturi_reduse)

data_ora="2023-04-24 09:03:32"
data_ora_filtrata=list(filter(lambda x: x, data_ora.replace("-", " ").split(" ")))
print("data ora filtrata:", data_ora_filtrata)

#!!!!!!
list1 = [1, 2, 3, 4, 5] 
list2 = [10, 20, 30, 40, 50] 
lista_suma=[]
for i, (l1, l2) in enumerate(zip(list1, list2)):
    lista_suma.append(l1 + l2)
print("suma listelor:", lista_suma)

lista_pare=[i for i in range(100) if i % 2 == 0]
print("numere pare pana la 100:", lista_pare)

lista_cuburi=[]
for i in range (0, 10):
    lista_cuburi.append(i**3)
print("lista cuburi:", lista_cuburi)

l1=[1, 2, 3]
l2=[2, 3, 4, 5, 6]
lista_comune=[]
for i in l1:
    if i in l2:
        lista_comune.append(i)
print("numere comune:", lista_comune)

set_pare={i*2 for i in range(10)}
print("set numere pare:", set_pare)

sir="Lucia este foarte frumoasa"
set_distincte={i for i in sir}
print("set distincte:", set_distincte)

set_5litere={i for i in sir.split(" ") if len(i)>=5}
print("set cu 5 litere:", set_5litere)

dictionar_patrate={i: i*i for i in range(10)}
print("dictionar patrate:", dictionar_patrate)

dictionar_litere_aparitii={i: sir.count(i) for i in sir}
print("dictionar litere aparitii:", dictionar_litere_aparitii)

dictionar_divizori={i:[j for j in range(1, i+1) if i % j == 0] for i in range(1, 11)}
print("dictionar divizori:", dictionar_divizori)