import random 

result = random.random()
print(result)
# Sonuç olarak 0 ile 1 arasında ondalıklı bir sayı üretiliyor.Uygulamayı her çalıştırdığımızda farklı bir sayı üretilir.
# 0.3358059969600725, 0.5225737109642167 şeklinde bu sonuç her seferinde değişir.

import random
result = random.random()*100 
print(result) 
# Sonuç olarak; üretilen sayı 100 ile çarpılır. (36.04195978092382)

import random
result = random.uniform(1,10)
print(result)
# Sonuç olarak ; 1 ile 10 arasında bir sayı üretir.Bu sayı yine ondalıklı olur. (7.4276101243396075)

# Aralıkları arttırmak istersek de (1,10) ya da (10,100) şeklinde tanımlamalar yapabiliriz.

# Üretilen sayılar ondalıklı olacak ama biz bunların tam kısmını almak istersek, yazdırmak istersek int kullanırız.

import random
result = int(random.uniform(10,100))
print(result) 
# Sonuç olarak; sistem her çalıştığında sonuç değişir. (80,22,23) şeklinde farklı sonuçlar gelir.

# Bu işlemin aynısını randint metoduyla yaparız.
import random
result = random.randint(1,100)
print(result)
# Sonuç olarak; Sistem çalıştırıldığında (48,22,93) şeklinde farklı sonuçlar gelir. 

# Liste içerisinden rastgele bir eleman almak istersem; index numarasını da belirtebilirim ya da sayısını bilmediğim kadar eleman 
# varsa (len) metodu kullanıp herhangi bir elemanı çekebilirim.

names = ['ali','yağmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)]
print(result)
# Sonuç olarak; sistem her çalıştığında sonuç değişecektir.Liste içinden rastgele bir eleman gelecektir.
# (deniz,ali,cenk,ali,yağmur şeklinde)

# Eğer listedeki eleman sayısını arttırıp sistemi çalıştırsam da hata almam.Çünkü index numaraları dinamik bir şekilde çalışıyor.

# Random içinde bu işi yapabilmek için de bir metot eklenmiş len metodu yerine bunu kullanmak daha kolay.

names = ['ali','yağmur','deniz','cenk','ahmet','efe']
result = random.choices(names)
print(result)
# Sonuç olarak sistem her çalıştığında sonuç değişir.
# ['cenk'],['efe'],['yağmur'],['efe'],['deniz'] şeklinde gelir.

# Sadece liste değil string bir ifade tanımlamak istersek,

greeting = 'Hello There'
result = random.choices(greeting)
print(result)
# Sonuç olarak, sistemi her çalıştırdığımızda sonuç değişir.
# l,T,e şeklinde sonuçlar gelir.

# Bir tane liste tanımlayalım.

liste = list(range(10))
result = liste
print(result)
# Sonuç olarak, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gelir.

# Eğer ben bu sayıların karışık olarak gelmesini istersem ;

liste = list(range(10))
random.shuffle(liste)
result = liste
print(result)
# Sonuç olarak, sistemi her çalıştırdığımda sonuç değişir.
# [0, 3, 8, 6, 9, 5, 2, 4, 7, 1]
# [5, 2, 6, 4, 8, 7, 3, 9, 0, 1]  şeklinde değişik sonuçlar elde edilir.

# Eğer bir liste tanımlar ve içinden rastgele sayı almak istersem sample metodu kullanılır.
liste = range(100)
result = random.sample(liste,3)
print(result)
# Bu şekilde yazdığımda 0-100 arası 3 tane sayı liste şeklinde yazdırılır.
# Sonuç olarak, sistemi her çalıştırdığımda sonuç değişir.
# [36, 92, 22]
# [33, 43, 60] 
# [66, 63, 89]  şeklinde değişik sonuçlar gelir.