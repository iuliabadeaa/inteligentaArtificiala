import functools
from getpass import getpass

# lis=[1, 3, 5, 6, 2]

# print("The sum of the list elements is: ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))

# print("The maximum element in the list is:",end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))


pj=getpass("Primul jucator a ales: ")
dj=getpass("Al doilea jucator a ales: ")

game=True
while game==True:
    if pj==dj:
        print("Remiza")
    elif pj=="piatra" and dj=="foarfeca":
        print("Primul jucator a castigat")
    elif pj=="foarfeca" and dj=="hartie":
        print("Primul jucator a castigat")
    elif pj=="hartie" and dj=="piatra":
        print("Primul jucator a castigat")
    else:
        print("Al doilea jucator a castigat")
    continua=input("Continui jocul? y/n")
    if continua=="n":
        game=False


def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("introduceti un numar: "))
print("fibonacci:", fibonacci(n))


def genereaza_factura(args, **kwargs):
    print("Clientul "+args+" a cumparat:")
    for produs, pret in kwargs.items():
        print("produs: "+produs+", pret: "+str(pret)+" lei")


nume_client="Ion"
produse={"laptop": 1500, "aspirator": 800, "mixer": 400}
genereaza_factura(nume_client, **produse)

def normalizare(numere):
    numere_normalizate=[]
    for i in numere:
        numere_normalizate.append(1/i)
    return numere_normalizate

numere=[1, 2, 3, 4, 5]
print("numere normalizate:", normalizare(numere))


result = map(lambda x: x**2, numere)
print("numere patrate:", list(result))

a=[(1,10),(-1,-3),(39,0),(12,15)]
sorted_a=sorted(a, key=lambda x: x[1])
print("lista sortata:", sorted_a)