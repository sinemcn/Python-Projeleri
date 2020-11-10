# Inheritance (Kalıtım): Class'ların birbirinden miras alma durumudur.

# Örneğin: Person => name,lastname,age,eat(),run(),drink() diyebiliriz.
# Bunlar bir person için temel olan görevlerdir.

# Student(Person), Teacher(Person)
# İlerleyen aşamada Student ve Teacher isminde bir class tanımlayacak olsam üstteki Person görevlerinin hepsi-
# nin Student ve Teacher'da olmasını da istersem; Student(Person) şeklinde algılanmasını sağlar,Person'dan 
# miras alma işlemini gerçekleştiririm. Teacher(Person) yaptığımızda da Person'daki her şey Teacher'a miras
# olarak aktarılır.

# Bu durumda Person için tanımlanan attributes'lar,özellikler Student ve Teacher için tanımlanır.Student için
# öğrenci numarası student class içine eklenebilir.Teacher içinde bir branş bilgisi eklenebilir ancak bu 
# Person'ı etkilemez.Student ve Teacher özellikleri Person'a gitmez.Person bizim için temel sınıftır.

# Animal => Dog(Animal),Cat(Animal)
# Animal'ın temel özelliklerini Dog ve Cat taşıdığı için Animal'dan miras alması yeterlidir.

# ÖRNEK;

# class Person():
#      def __init__(self):
#           print('Person Created')

# class Student(Person):
#      pass

# p1 = Person()
# s1 = Person()

# Sonuç :
# Person Created 
# Person Created  gelecektir. 
# Bunun nedeni Student(Person) olduğu için s1 = Person() çağırdığımızda Person içindeki miras olarak aktarılır.

class Person():
     def __init__(self):
          print('Person Created')

class Student(Person):
     def __init__(self):
          Person.__init__(self)
          print('Student Created')

p1 = Person()
s1 = Student()

# Sonuç: 
# Person Created
# Person Created
# Student Created şeklinde gelecektir.

class Person():
     def __init__(self):
          print('Person Created')

class Student(Person):
     def __init__(self):
          print('Student Created')

p1 = Person()
s1 = Student()
# Sonuç: 
# Person Created
# Student Created şeklinde gelecektir.

# Person.__init__(self)'i Student'tan çağırıyoruz.Çünkü Person class'ının birçok özelliği olabilir.
class Person():
     def __init__(self,fname,lname):
          self.firstName = fname
          self.lastName = lname
          print('Person Created.')

class Student(Person):
     def __init__(self,fname,lname):
          Person.__init__(self,fname,lname)
          print('Student Created.')
     
p1 = Person('Sinem','Can')
s1 = Student('Uygar','Can')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)

# Sonuç: 
# Sinem Can
# Uygar Can  şeklinde gelir.

# EĞER PERSON'A BİRKAÇ TANE METOD EKLER VE STUDENT'TA NASIL ÇALIŞTIĞINA BAKMAK İSTERSEK;
class Person():
     def __init__(self,fname,lname):
          self.firstName = fname
          self.lastName = lname
          print('Person Created.')
     def who_am_i(self):
          print('I am a person.')

class Student(Person):
     def __init__(self,fname,lname):
          Person.__init__(self,fname,lname)
          print('Student Created.')

p1 = Person('Sinem','Can')
s1 = Student('Uygar','Can')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)

p1.who_am_i()
s1.who_am_i()

# Sonuç olarak:
# I am a person.
# I am a person.  şeklinde gelecektir.

class Person():
     def __init__(self,fname,lname):
          self.firstName = fname
          self.lastName = lname
          print('Person Created.')
     def who_am_i(self):
          print('I am a person.')
     
     def eat(self):
          print('I am eating.')

class Student(Person):
     def __init__(self,fname,lname):
          Person.__init__(self,fname,lname)
          print('Student Created.')

p1 = Person('Sinem','Can')
s1 = Student('Uygar','Can')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()

# SONUÇ OLARAK ;
# Person Created.
# Person Created.
# Student Created.
# Sinem Can
# Uygar Can
# I am a person.
# I am a person.
# I am eating.
# I am eating.      şeklinde gelecektir.

# Eğer def who_am_i(self)'i Student üzerinden çağırırsak sonuç Student için yazılan print'ten gelir.
class Person():
     def __init__(self,fname,lname):
          self.firstName = fname
          self.lastName = lname
          print('Person Created.')
     def who_am_i(self):
          print('I am a person.')
     
     def eat(self):
          print('I am eating.')

class Student(Person):
     def __init__(self,fname,lname):
          Person.__init__(self,fname,lname)
          print('Student Created.')
     def who_am_i(self):
          print('I am a student.')

p1 = Person('Sinem','Can')
s1 = Student('Uygar','Can')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
# SONUÇ OLARAK ;
# Person Created.
# Person Created.
# Student Created.
# Sinem Can
# Uygar Can
# I am a person.
# I am a student.  # Aynı isimdeki bir metot temel sınıftaki metodu ezer. Buna #override denir.I am a student şeklinde değiştirilir !
# I am eating.
# I am eating.

# EĞER STUDENT'A ÖZEL OLAN BİLGİLERİ KULLANMAK İSTERSEK STUDENT ÜZERİNDEN FONKSİYON YAZILIR. !

class Person():
     def __init__(self,fname,lname,):
          self.firstName = fname
          self.lastName = lname
          print('Person Created.')
     def who_am_i(self):
          print('I am a person.')
     
     def eat(self):
          print('I am eating.')

class Student(Person):
     def __init__(self,fname,lname,number):
          Person.__init__(self,fname,lname)
          self.studentNumber = number
          print('Student Created.')
     
     def who_am_i(self):
          print('I am a student.')
     
     def sayHello(self):
          print('Hello I am a student.')

p1 = Person('Sinem','Can')
s1 = Student('Uygar','Can',641)

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

s1.sayHello()
# Sonuç : 
# Uygar Can 641
# Hello I am a student.  şeklinde gelecektir.

# BİR TANE DE TEACHER CLASS'I TANIMLAYALIM.
class Teacher(Person):
     def __init__(self,fname,lname,branch):
          super().__init__(fname,lname)
          self.branch = branch
     def who_am_i(self):
          print(f'I am a {self.branch} teacher')
t1 = Teacher('Emine','Can','Math')
t1.who_am_i()

# Sonuç olarak : I am a Math teacher yazacaktır.