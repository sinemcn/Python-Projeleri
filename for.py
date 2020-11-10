numbers = [1,2,3,4,5]

for num in numbers:
     print(num)

for a in numbers:
     print('Hello')

names = ['Sinem', 'Uygar', 'Sibel']

for name in names:
     print(f'My name is {name}.')

name = 'Sinem Can'

for n in name:
     print(n) # Harfler aşağı doğru tek tek yazılır.

tuple = (1,2,3,4,5)

for t in tuple:
     print(t) 

tuple = [(1,2),(1,3),(3,5),(5,7)]
for t in tuple:
     print(t)

for a,b in tuple:
     print(a,b)
for a,b in tuple:
     print(a)     # Sadece 1,1,3,5 yazılır.
for a,b in tuple:
     print(b)     # Sadece 2,3,5,7 yazılır.

# Eğer dictionary şeklinde yazdırmak istersek:

d = {'k1': 1, 'k2': 2, 'k3': 3 }
for item in d:
     print(item)  # Şeklinde yazarsak sadece key bilgisi olan 
#k1
#k2 
#k3 yazılır.

for item in d.items():
     print(item)  
# Şeklinde yazarsak hem key hem de value değerleri yazılır. 
#('k1', 1)
# ('k2', 2) 
# ('k3', 3) olarak yazılır.

for key,value in d.items():
     print(key,value)  # k1 1 
                       # k2 2 
                       # k3 3 şeklinde yazılır.
