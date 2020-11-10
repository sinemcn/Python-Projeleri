for x in range(10):
     print(x)   # Bu şekilde yazdırdığımızda 0'dan başlar ve 10'a kadar yazılır.

numbers = [x for x in range(10)]
print(numbers)   # Bu şekilde yazdırdığımızda liste içinde hazır bir şekilde yazdırılır.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = []
for x  in range(10):
     numbers.append(x)
print(numbers)   # Append metoduyla da bu işlem yapılabilir.Listenin içine verilen range değeri yerleştirilir.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
     print(x**2)
# Sonuç : 
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81    şeklinde yazılır.

numbers = [x**2 for x in range(10)]
print(numbers)
# Sonuç :
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers = [x*x for x in range(10)]
print(numbers)
# Sonuç: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] çıkacaktır.

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)  # Burada 0'dan 10'a kadar olan sayılarda sadece 3'e bölünen sayıları yazdırırız.
# Sonuç: [0, 9, 36, 81]  olarak çıkacaktır.

myString = 'Hello'
myList = []

for letter in myString:
     myList.append(letter)
print(myList)
# Sonuç: ['H', 'e', 'l', 'l', 'o']  çıkar.

myList = [letter for letter in myString]
print(myList)
# Sonuç: ['H', 'e', 'l', 'l', 'o']  yine aynı şekilde yazılır.

years = [1983, 1999, 2008, 1956, 1986] 
ages = [2020-year for year in years]
print(ages)
# Sonuç: [37, 21, 12, 64, 34] şeklinde liste içinde yazdırılır.

results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)
# Sonuç: ['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']  şeklinde yazılır.

result = []

for x in range(3):
     for y in range(3):
          result.append((x,y))
print(result)
# Sonuç: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
# Sonuç: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] şeklinde yine aynısı olur.

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
# SONUÇ:
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), 
# (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), 
# (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)] şeklinde gelir.

