# x = 0
# while x < 5:
#      x += 1
#      if x == 2:
#           continue
#      print(x)

# x = 1
# toplam = 0
# while x <= 100:
#      toplam += x
#      x+=1
# print(f'toplam: {toplam}')

# x = 1
# toplam = 0
# while x <= 100:
#      x+=1
#      if x %2 == 1:
#           continue
#      toplam += x
# print(f'toplam: {toplam}')

# x = 1
# toplam = 0
# while x <=100:
#      x+=1
#      if x == 2:
#           continue
#      toplam += x
# print(f'toplam: {toplam}')

# def changeName(n):
#      n = 'ada'
# name = 'sinem'    
# changeName(name)
# print(name)

# def add(*params):
#      print(params)
#      print(params[0])
#      print(params[2])
#      return(sum(params))


# print(add(10,20,50))
# print(add(10,20,30))
# print(add(10,20,30,50,60,10,20))


# def square (num):
#      return num ** 2
# numbers = [1,3,5,7]
# result = square(numbers)
# print(result)


# birthday = 2008
# calculateAge = (2020-birthday)
# print(calculateAge)

# class Person():
#      def __init__(self):
#           print('Person Created')

# class Student(Person):     
#      def __init__(self):
        
#           print('Student Created')

# p1 = Person()
# s1 = Student()

# class Movie():
#      def __init__(self,title,director,duration):
#           self.title = title
#           self.director = director
#           self.duration = duration
#           print('Movie objesi oluşturuldu.')
     
#      def __str__(self):
#           return f"{self.title} by {self.director}"

#      def __del__(self):
#           print('Film objesi silindi.')

# m = Movie('filmin adı','yönetmen adı','filmin süresi')
# # print(str(m))

sayı = 19
result = 5
carpım = 19*5

print("{} ile {} in çarpımı {} eder.".format(sayı,result,carpım))