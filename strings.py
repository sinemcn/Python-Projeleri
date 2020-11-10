name = "Sinem"
surname = " Can"
age = '24'

print('My name is '  + name + ' ' + surname + ' and I am '+ age + ' years old. ') 
print('My name is '  + name + ' ' + surname + ' and  \nI am '+ age + ' years old.') 

greeting = 'My name is ' + name + ' ' + surname + ' and  \nI am '+ age + ' years old'
length = len(greeting)

# print(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[2])
print(len(greeting))
print(greeting[length-1])

# Bu kadar işlem yapmak yerine print(greeting[-1]) yazarsak yani indeks numarasını yazarsak yine d çıkacaktır !
print(greeting[-1])

print(greeting[0])  # M çıkar.
print(greeting[4])  # a çıkar.

# İndeks numaralarını yazarken : print(greeting[2:]) yazılırsa sondan 2 karakter bulunur.
# İndeks numaları yazarken : print(greetin[2:5]) yazılırsa 2'den 5'e kadar olan karakterler yazılır. Yani 2=Boşluk 3=n 4=a olur !

print(greeting[2:5])
print(greeting[3:7])

# İndeks numarasını yazar sonuna kadar yazmak istersek bitişi yazmak zorunda kalmayız. print(greeting[3:])şeklinde yazılabilir.
# Bu durumda 3 ten başlar son karaktere kadar yazılır.
print(greeting[3:])
# İndeksi baştan al son karakter 16 olsun dersek : print(greeting[:16]) yazılır.
print(greeting[:16])

# İndeks numarasını 2'den başla 40'a kadar git ancak her karakteri alma 2 karakterde bir al demek için print(greeting[2:40:2])olarak yazılır.
print(greeting[2:40:2])
print(greeting[2:40:1])
print(greeting[2:40:3])

