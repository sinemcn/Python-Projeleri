# Yöntem 1 

import math 

value = dir(math)
print(value)        # Math modülü içerisinde bulunan bütün fonksiyonlar karşımıza gelir.

# Eğer bu fonksiyonlar hakkında bilgi sahibi olmak istersek, sadece isimler yetmiyor dersek;

# import math 
# value = help(math)
# print(result)       # Math'in yardım dökümanını sistem yazar.Enter a basarak terminalde ilerlersek döküman içindekiler çıkar.

# Eğer tek bir fonksiyon kullanımını görmek istersek;

# import math 

# value = help(math.factorial)
# print(value)          # Bu şekilde factorial in nasıl çalıştığı karşımıza gelir.Hangi parametreleri aldığını bize açıklar.

# ÖRNEKLER;
# value = math.sqrt(49)     # sqrt : Karekök demektir. 49'un karekökü 7.0 şeklinde gelir.
# value = math.factorial(5) # factorial : Faktöriyel elde edilir. Sonuç 120 şeklinde gelir.
# value = math.floor(5,9)   # floor : Sayıyı aşağıya doğru yuvarlar. Sonuç : 5 olarak gelir.
# value = math.ceil(5,9)    # ceil : Sayıyı yukarı doğru yuvarlar. Sonuç : 6 olarak gelir.

# print(value)


# Eğer import math e takma bir isim vermek istersek;

# import math as islem   

# value = islem.factorial(5)
# print(value)                
# Sonuç : Yine 120 gelir.Kütüphaneye işlem takma ismiyle ulaşabiliriz.

# YÖNTEM 2 

# Burada import ettiğimiz kütüphane için direk import demek yerine from math diyoruz.

# Eğer ilgili kütüphaneden hepsini import et dersem; * kullanmam gerekir.

# from math import*

# value = factorial(5)   # Sonuç : 120
# value = sqrt(9)        # Sonuç : 3.0   şeklinde gelir.
# print(value)               

# Eğer kullanıcak olduğum metodları yazdırmak istersem;

# from math import factorial,sqrt

# value = factorial(5)      # Sonuç : 120
# value = sqrt(9)           # Sonuç : 3.0   şeklinde gelir.
# print(value)

# Şu durumda kütüphane içinden 2 tane fonksiyon import ettim.Eğer import etmediğim 3.değeri yazmak istersem sistem ERROR verir.
# from math import factorial,sqrt

# value = factorial(5)
# value = sqrt(9)
# value = ceil(9.8)
# print(value)
# Sonuç : 
# 120
# 3,0
# value = ceil(9.8)
# NameError: name 'ceil' is not defined  şeklinde sonuç gelir ve 3.fonksiyon yazılmaz.

# 3.değeri import ettiğimizde sistem çalışır.

from math import factorial,sqrt,ceil

value = factorial(5)
value = sqrt(9)
value = ceil(9.8)
print(value) 

# Sonuç : 
# 120 
# 3.0 
# 10 olarak gelir.

# Biz başka bir modülden ya da şuan oluşturmuş olduğumuz dosya içinden yine aynı isimli bir fonksiyon tanımlamış olsak python hangi 
# fonksiyonu kullanacak biz buna bakalım.

def sqrt(x):
     print('x:' + str(x))

from math import factorial,sqrt,ceil

value = sqrt(9)
print(value)  
# Sonuç : 3.0 olarak gelir.

# Eğer biz def sqrt(x) fonksiyonunu from math import'tan sonra yazsaydık sonuç 9 olarak gelirdi.En son yazdığımız değer 9 algılanır.
# Karekökü alınmaz.Fonksiyon ezilir.

