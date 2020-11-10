# class 
class Person():
     # class attributes
     address = 'no information'
     # constructor (yapıcı metod)
     def __init__(self,name,year):
          #object attributes
          self.name = name
          self.year = year
     # instance methods
     def intro(self):
          print('Hello There.I am ' + self.name)
#object (instance)
p1 = Person(name = 'Sinem', year = 1996)
p2 = Person(name = 'Gizem', year = 1997)

p1.intro()
p2.intro()

# Sonuç : 
# Hello There.I am Sinem
# Hello There.I am Gizem   şeklinde olacaktır.

# Bir tane daha instance metodu ekleyelim.
class Person():
     address = 'no information'

     def __init__(self,name,year):
          self.name = name
          self.year = year
     def intro(self):
          print('Hello There.I am '+ self.name)
     def calculateAge(self):
          return 2020-self.year
p1 = Person(name = 'Sinem', year = 1996)
p2 = Person(name = 'Gizem', year = 1997)

p1.intro()
p2.intro()

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')
# Sonuç:
# adım: Sinem ve yaşım: 24
# adım: Gizem ve yaşım: 23  şeklinde gelecektir.

###########################################################

# Yeni bir class ekleyelim.
class Circle: 
     pi = 3.14

     def __init__(self,yaricap=1):
          self.yaricap = yaricap
     def cevre_Hesapla(self):
          return 2*self.pi*self.yaricap
     def alan_hesapla(self):
          return self.pi*(self.yaricap**2)
c1 = Circle()
c2 = Circle(5)

print(f'c1: alan: {c1.alan_hesapla()} çevre: {c1.cevre_Hesapla()}')
print(f'c2: alan: {c2.alan_hesapla()} çevre: {c2.cevre_Hesapla()}')
# Sonuç: 
# c1: alan: 3.14 çevre: 6.28
# c2: alan: 78.5 çevre: 31.40  şeklinde gelecektir.

# pi = 3,14 değerini class attributes olarak tanımlamamızın sebebi hepsi için ortak bir değer olmasıdır.
# Eğer class şeklinde değil de constructor olarak yazmak istersek her seferinde pi = 3.14 değerini fonksiyonun
# üstüne yazmak zorunda kalırız.