# RANGE METODU

for item in range(10):
     print(item)
# Burada range metoduna 10 değerini verdiğimizde ve sistemi çalıştırdığımızda bize 0'dan 10'a kadar olan
# tüm sayıları yazar. (10 hariç) (0,1,2,3,4,5,6,7,8,9)

for item in range(2,10):
     print(item)
# Bu durumda sisteme 2'den başla 10'a kadar git komutunu veririz.

for item in range(50,100,10):
     print(item)
# Bu durumda sisteme 50'den başla, 100'e kadar 10'ar 10'ar git komutu verilir.
# Aralığı arttırmak istersek bu durumda 10 değil 20 yazarız ya da istediğimiz kadar arttırırız.

# Range metodunun içindeki elemanları bir liste şeklinde yazmak istersek;
print(list(range(50,100,10)))  #şeklinde yazarız ! [50,60,70,80,90]

print(list(range(5,100,10))) # 5'ten başla 100'e kadar 10'ar 10'ar yaz demektir!
# Sonuç: [5,15,25,35,45,55,65,75,85,95] olur.

# ENUMERATE METODU

greeting = 'Hello'

for letter in greeting:
     print(letter)  # Elemanlar aşağı doğru tek tek yazılır.

# Eğer yazdırdığımız karakterlerin indeks numarasına da ulaşmak istersek; bir indeks değişkeni tanımlarız.

index = 0
greeting = 'Hello'

for letter in greeting:
     print(f'index: {index}, letter: {letter}')
     index += 1

# Sistemi bu şekilde de çalıştırabiliriz aynı sonucu verecektir.
index = 0
greeting = 'Hello'

for letter in greeting:
     print(f'index: {index}, letter: {greeting[index]}')
     index += 1

# index: 0, letter: H
# index: 1, letter: e
# index: 2, letter: l
# index: 3, letter: l
# index: 4, letter: o   =====>>>>> SONUÇ bu şekilde gelir !

# ENUMERATE METODUYLA ÇALIŞTIRMAK İSTERSEK;
 
greeting = 'Hello'

for index,letter in enumerate(greeting):
     print(f'index: {index}, letter: {letter}')

# Eğer index yerine item yazarsak;
greeting = 'Hello'

for item in enumerate(greeting):
     print(item)
# Sonuç: 
# (0,'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')  İNDEKSLERİ VE KARAKTERLERİ BİZİM İÇİN BİR LİSTE ŞEKLİNDE OLUŞTURUR !

# Listenin elemanlarına ulaşmak istediğimde;
greeting = 'Hello'

for index,item in enumerate(greeting):
     print(f'index: {index}, letter: {item}')   # yazarım ve liste içindeki elemanlara ulaşırız.

# index: 0, letter: H
# index: 1, letter: e
# index: 2, letter: l
# index: 3, letter: l
# index: 4, letter: o   şeklinde yazılır.


# ZIP METODU:

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip(list1,list2)))

# Sonuç : [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

print(list(zip(list1,list2,list3)))

# Sonuç : [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1,list2,list3):
     print(item)
# Sonuç: 
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
# (4, 'd', 400)
# (5, 'e', 500)

for a,b,c in zip(list1,list2,list3):
     print(a)   # Sadece a'nın değerini almak istersek a'yı yazdırırız.

# Sonuç: 
# 1
# 2
# 3
# 4
# 5

for a,b,c in zip(list1,list2,list3):
     print(a,b,c) 

# Sonuç: 
# 1 a 100
# 2 b 200
# 3 c 300
# 4 d 400
# 5 e 500    şeklinde gelecektir.