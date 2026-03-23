# Tipuri de date
type(1)      # int
type(-10)    # int
type(0)      # int
type(0.0)    # float
type(2.2)    # float
type(4E2)    # float - 4*10 la puterea 2

# Aritmetică
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 ** 3  # 1000
10 / 3   # 3.3333333333333335
10 // 3  # 3 -> împărțire întreagă (fără zecimale)
10 % 3   # 1 -> modulo (restul împărțirii)

# Basic Functions
pow(5, 2)        # 25 --> ca 5**2
abs(-50)         # 50
round(5.46)      # 5
round(5.468, 2)  # 5.47 --> rotunjire la 2 zecimale
bin(512)         # '0b1000000000' --> format binar
hex(512)         # '0x200' --> format hexazecimal

# Converting Strings to Numbers
age = input("How old are you?")
age = int(age)

pi = input("What is the value of pi?")
pi = float(pi)


# Strings
type('Helloooooo')  # str

'Im thirsty'
"I'm thirsty"
"\n"  # newline
"\t"  # tab

'Hey you!'[4]  # y

name = 'John Doe'

print(name[2])    # h
print(name[:])    # John Doe
print(name[1:])   # ohn Doe
print(name[:1])   # J
print(name[-1])   # e
print(name[::1])  # John Doe
print(name[::-1]) # eoD nhoJ
print(name[0:7:2]) # Jh o

# slicing format: [start : end : step]

# String concatenation
print('Hi there ' + 'Timmy')  # Hi there Timmy

# Repetition
print('*' * 10)  # **********

# Palindrome check
word = 'reviver'
# .find() returnează 0 dacă găsește subșirul, sau -1 dacă nu. 
# Adunând 1, transformăm -1 în 0 (False) și 0 în 1 (True).
p = bool(word.find(word[::-1]) + 1)
print(p) # True

# Toate de mai jos evaluează la False. Orice altceva va fi True.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))      # Listă goală
print(bool({}))      # Dicționar gol
print(bool(()))      # Tuplu gol
print(bool(''))      # String gol
print(bool(range(0)))
print(bool(set()))   # Set gol

my_list = [1, 2, '3', True] # Presupunem că lista nu se modifică pentru exemplele de slicing

len(my_list)               # 4
my_list.index('3')         # 2
my_list.count(2)           # 1 (de câte ori apare 2)

# Slicing [start:end:step]
my_list[3]                 # True
my_list[1:]                # [2, '3', True]
my_list[:1]                # [1]
my_list[-1]                # True
my_list[::1]               # [1, 2, '3', True]
my_list[::-1]              # [True, '3', 2, 1] (inversare)
my_list[0:3:2]             # [1, '3']

# Adăugare în listă
my_list * 2                # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100]            # [1, 2, '3', True, 100] (creează o listă nouă)

my_list.append(100)        # Mută lista originală: [1, 2, '3', True, 100]
my_list.extend([100, 200]) # Mută lista originală: [1, 2, '3', True, 100, 100, 200]
my_list.insert(2, '!!!')   # Inserează la indexul 2: [1, 2, '!!!', '3', True...]

' '.join(['Hello', 'There']) # 'Hello There' (unește elementele unui string)

# Copiere listă
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

# Eliminare din listă
[1, 2, 3].pop()            # Returnează 3 și modifică lista (default ultimul item)
[1, 2, 3].pop(1)           # Returnează 2 (elementul de la index 1)
[1, 2, 3].remove(2)        # Elimină prima apariție a valorii 2
[1, 2, 3].clear()          # Golirea listei: []
# del [1, 2, 3][0]         # Șterge elementul de la indexul 0

# Ordonare
[1, 2, 5, 3].sort()        # Modifică în: [1, 2, 3, 5]
[1, 2, 5, 3].sort(reverse=True) # [5, 3, 2, 1]
[1, 2, 5, 3].reverse()     # Inversează ordinea: [3, 5, 2, 1]
sorted([1, 2, 5, 3])       # Returnează o listă NOUĂ: [1, 2, 3, 5]
list(reversed([1, 2, 5, 3])) # [3, 5, 2, 1]

# Operații utile
1 in [1, 2, 5, 3]          # True
min([1, 2, 3])             # 1
max([1, 2, 3])             # 3
sum([1, 2, 3])             # 6

# Unpacking (Despachetare)
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first)               # 63
print(last)                # 10

# Citire fișier într-o listă
# with open("myfile.txt") as f:
#     lines = [line.strip() for line in f]

my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}

my_dict['name']            # 'John Doe'
len(my_dict)               # 3
list(my_dict.keys())       # ['name', 'age', 'magic_power']
list(my_dict.values())     # ['John Doe', 25, False]
list(my_dict.items())      # [('name', 'John Doe'), ('age', 25), ...]

my_dict['favourite_snack'] = 'Grapes' # Adăugare cheie nouă

my_dict.get('age')         # 25 (Returnează None dacă nu există)
my_dict.get('ages', 0)     # 0 (Returnează valoarea default 0 dacă nu găsește cheia)

# Eliminare cheie
del my_dict['name']
my_dict.pop('name', None)

my_tuple = ('apple', 'grapes', 'mango', 'grapes')
apple, grapes, mango, grapes_2 = my_tuple # Unpacking
len(my_tuple)              # 4
my_tuple[2]                # 'mango'
my_tuple[-1]               # 'grapes'

# Imutabilitate (Vor genera erori):
# my_tuple[1] = 'donuts'   # TypeError
# my_tuple.append('candy') # AttributeError

# Metode
my_tuple.index('grapes')   # 1
my_tuple.count('grapes')   # 2

my_set = set()
my_set.add(1)              # {1}
my_set.add(100)            # {1, 100}
my_set.add(100)            # {1, 100} -> Fără duplicate!

new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
set(new_list)              # {1, 2, 3, 4, 5, 6}

my_set.remove(100)         # Ridică KeyError dacă nu găsește elementul
my_set.discard(100)        # NU ridică eroare dacă nu găsește elementul
my_set.clear()             # {}
new_set = {1, 2, 3}.copy()

# Operații cu seturi
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)                 # {1, 2, 3, 4, 5}
set4 = set1.intersection(set2)          # {3}
set5 = set1.difference(set2)            # {1, 2}
set6 = set1.symmetric_difference(set2) # {1, 2, 4, 5}

set1.issubset(set2)        # False
set1.issuperset(set2)      # False
set1.isdisjoint(set2)      # False (Returnează True dacă nu au elemente comune)

# Frozenset (Imutabil și Hashable - poate fi cheie în dicționar)
# f_set = frozenset([1, 2, 3])