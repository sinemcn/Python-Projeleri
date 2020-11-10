def changeName(n):
     n = 'ada'

name = 'Yiğit'

changeName(name)
print(name)


def change(n):
     n[0] = 'istanbul'
sehirler = ['ankara', 'izmir']
change(sehirler)
print(sehirler)


def change(n):
     n[0] = 'istanbul'

sehirler = ['ankara','izmir']
n = sehirler

n[0] = 'istanbul'
print (sehirler)

def change(n):
     n[0] = 'istanbul'

sehirler = ['ankara','izmir']
n = sehirler[:]  # sehirler içindeki tüm elemanları n nin içine atalım.
# Buna slicing denir. Orjinal listeye dokunmamış oluruz.
n[0] = 'istanbul'
print (sehirler)
print(n)         # Sonuç : ['ankara', 'izmir']
                 #         ['istanbul', 'izmir'] şeklinde gelir.

# Orjinal listeyi bozmak istemezsek ve fonksiyon şeklinde yazdırırsak;

def change(n):
     n[0] = 'istanbul'
sehirler = ['ankara','izmir']

change(sehirler[:])
print(sehirler)  # Sonuç: ['ankara', 'izmir'] gelir.


def add(a, b):
     return sum((a,b))
print(add(10,20))   # Sonuç: 30

def add(a, b, c = 0):
     return sum((a,b,c))
print(add(10,20,30)) # Sonuç: 60

def add(a,b,c = 0, d = 0,e = 0):   # Bu şekilde en fazla 5 tane tanımlama yapılır.
     return sum((a,b,c)) 
print(add(10,20,30))

# 5'ten fazla parametre tanımlamak istersek şu işlem yapılır.

def add(*params):
     return sum((params))
print(add(10,20))     
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))
# Sonuç: 30, 60, 200 şeklinde gelecektir.

# Bu durumda params'ı print ile yazdırmak istersek; bu bize tuple şeklinde elemanları verecktir.
# fonksiyonun hemen altına print(params) yazdırmak zorundayız.

def add(*params):
     print(params)
     return sum((params))
print(add(10,20))     
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))

# Tuple şeklinde gelen elemanların bu durumda indeks numarasıyla elemanlarına da ulaşabilirim.

def add(*params):
     print(params[0])  # Sonuç: 10,50
     print(params[2])  # Sonuç: 10,30
     return sum((params))
print(add(10,20,50))     
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))  # Sonuç: params[0] = 10, params[2] = 30 şeklinde yazılır.

# sum Fonksiyonunu kullanmak istemezsek;

def add(*params):
     sum = 0
     for n in params:
          sum = sum + n 

     return sum

print(add(10,20,50))    # Sonuç: 80 
print(add(10,20,30))    # Sonuç: 60
print(add(10,20,30,50,60,10,20)) # Sonuç: 200



def displayUser(**args):
     print(type(args))
     for key,value in args.items():
          print('{} is {}'.format(key,value))


displayUser(name = 'Sinem', age = 24, city = 'Ankara')
displayUser(name = 'Uygar', age = 12, city = 'Ankara', phone = '12345')
displayUser(name = 'Gizem', age = 23, city = 'Ankara', phone = '1231456', email = 'gizem@gmail.com')

# Sonuç : 

# <class 'dict'>
# name is Sinem
# age is 24
# city is Ankara
# <class 'dict'>
# name is Uygar
# age is 12
# city is Ankara
# phone is 12345
# <class 'dict'>
# name is Gizem
# age is 23
# city is Ankara
# phone is 1231456
# email is gizem@gmail.com   ===>>> şeklinde gelecektir.

def myFunc(a,b,c,*args,**kwargs):
     print(a)
     print(b)
     print(c)
     print(args)
     print(kwargs)

myFunc(10,20,30,40,50,key1 = 'value 1', key2 = 'value 2')

# Sonuç olarak :
# 10
# 20
# 30
# (40, 50)
# {'key1': 'value 1', 'key2': 'value 2'}  şeklinde gelir.