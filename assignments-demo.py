x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ? 

a = int(input("1.sayı: "))
b = int(input("2.sayı: "))

result = (a * b) - (x+y+z)
 
# 1.sayı için 10, 2.sayı için 20 dediğimizde çarpımları 200 çıkar. 
# # x+y+z = 17 sonucunu 200 den çıkarırsak 183 sonucunu elde ederiz !

# 2- y' nin x'e kalansız bölümünü hesaplayınız.
x = 2
y = 5 
a = y // x
print(a)

# 3- (x,y,z) toplamının mod 3 ü nedir ?
toplam = (x+ y+ z)
result = toplam % 3

# 4- y'nin x.kuvvetini hesaplayınız.
result = y **x
# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
print(y)  # Sonuç olarak : [5,7,10] çıkacaktır !
print(z)  # Sonuç : 6 çıkar.
result = z **3
# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ? 
# result = y => [5,7,10] gelir.
result = y[0] + y[1] + y[2]  # Sonuç : 22 çıkar.


print(result)