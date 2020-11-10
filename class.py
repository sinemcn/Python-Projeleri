# Bir Class tanımlayalım.Class tanımlamak için class key word'ü kullanılır ve isim verilir.Büyük harfle başlanır.

# class Person:
     # attributes
     # methods     tanımlamamız gerekir.(İki noktadan sonra)
# Sistemi bu şekilde çalıştırırsak hata verir.Bunun nedeni class Person: 'dan sonra kod eklememiz gerektiğidir.

# Sistemi çalıştırmak için bir yer tutucu olan pass tanımlayalım.
# class Person:
#      pass
# Uygulamayı bu durumda çalıştırırsak bir hata almayız.Boş bir class tanımlaması yaptık ve pass key word'ü yer
# tutucu olarak kullandık.Kod girmememize rağmen sistem hata vermedi.

# Object (instance) ==> Küçük harfle başlar.
# p1 = Person()
# print(p1)

# Sonuç olarak : <__main__.Person object at 0x000001AA334F0F48>  gelecektir. Bu sonuç p1 objesinin belirtilen 
# bir adreste Person tipi olduğunu söylüyor.

# p2 = Person()
# print(p2) 

# # Sonuç olarak: <__main__.Person object at 0x0000015BA76B0F88> gelecektir. Farklı adreste tanımlanmış bir
# # Person tipi olan p2 objesini yazdırmış oluruz.

# print(type(p1))
# print(type(p2))  
# Sonuç olarak her ikisi için de ;
# <class '__main__.Person'>
# <class '__main__.Person'>  gelecektir.

# print(p1 == p2) # Sonuç FALSE çıkar. Çünkü adresleri farklıdır.

# class 
class Person():
     pass
     #class attributes 

     #object attributes 
     #constructor 

# Constructor tanımlaması için yapmamız gereken bir metot tanımlamasıdır.Bunu __init__ metoduyla yaparız.
# Bu metodun parametreleri olacak.

     #constructor (yapıcı metod)
     def __init__(self,name,year):
          #object attributes
          self.name = name
          self.year = year
          print('init metodu çalıştı.')

# Self = class'ta türetilen p1 ya da p2 objesi.

p1 = Person('Ali',1990)
p2 = Person('Yağmur',1995)

# Sonuç : 
# init metodu çalıştı.
# init metodu çalıştı.   şeklinde gelecektir.

print(f'p1: name: {p1.name} year: {p1.year}')
print(f'p2: name: {p2.name} year: {p2.year}')

# Sonuç: 
# p1: name: Ali year: 1990
# p2: name: Yağmur year: 1995   şeklinde gelecektir.

# Class Attributes 
class Person():
     address = 'no information'

     def __init__(self,name,year):
          self.name = name
          self.year = year
          print('init metodu çalıştı.')

p1 = Person('Sinem',1996)
p2 = Person('Gizem',1997)

print(f'p1: name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2: name: {p2.name} year: {p2.year} address: {p2.address}')

# Sonuç : 
# p1: name: Sinem year: 1996 address: no information
# p2: name: Gizem year: 1997 address: no information    şeklinde gelir.

# EĞER ADRES ÜZERİNDE BİR DEĞİŞİKLİK YAPMAK İSTERSEK UPDATE EDERİZ.
p1.name = 'Emine'
p1.address = 'Ankara'

print(f'p1: name: {p1.name} year: {p1.year} address: {p1.address}')

# Sonuç: (p1: name: Emine year: 1996 address: Ankara)  şeklinde güncellenir.


