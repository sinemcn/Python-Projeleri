import mod 

# import mod yazıp sistemi çalıştırdığımızda otomatik olarak Modül eklendi yazacaktır.
# Biz modülümüze import mod dediğimizde mod.py içinde çalıştırılabilir olan bir kod varsa o direk çalıştırılır.

# import mod dedikten sonra modül hakkında bilgi almak isteyelim.
import mod 

result = help(mod)
print(result)
# Sistem modül hakkında tüm bilgileri terminalde yazar.Enter'a bastıkça aşağı doğru bilgiler ortaya çıkar.

# Eğer help metoduyla modülün içindeki fonksiyonun açıklamasını yazdırmak istersem;

import mod 
result = help(mod.func)
print(result)
# Sonuç olarak ;
# Help on function func in module mod:

# func(x)   gelecektir.

import mod 
result = mod.number
print(result)
# Sonuç olarak ; 10 gelir.

import mod 
result = mod.numbers
print(result)
# Sonuç olarak ; [1,2,3] gelir.

import mod 
result = mod.person["name"]
print(result)
# Sonuç olarak ; Ali gelir.

import mod 
result = mod.person["age"]
print(result)
# Sonuç olarak ; 25 gelir.


# Eğer fonksiyonu çalıştırmak istersek; fonksiyona bir parametre verip sistemi çalıştırırız.

import mod 
result = mod.func(10)
print(result)
# Sonuç olarak ; x: 10 gelir.

# Bir person tanımlayalım bunu direk mod.person üzerinden alacağız, bir obje tanımlamış olacağız ve obje üzerinden speak dediğimiz
# zaman bu ekrana gelip 'I am speaking' i yazdırır.

p = mod.Person()
p.speak()
# Sonuç olarak ; I am speaking  yazacaktır.







