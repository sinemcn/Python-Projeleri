sayilar = [1,3,5,7,9,12,19,21]
# 1- sayilar listesindeki hangi sayılar 3'ün katıdır?
for sayı in sayilar:
     if sayı %3 == 0:
          print(sayı)
# 2- sayilar listesindeki sayıların toplamı kaçtır?
toplam = 0
for sayı in sayilar:
     toplam += sayı
print('toplam:',toplam)
# 3- sayilar listesindeki tek sayıların karesini alınız.
for sayı in sayilar:
     if sayı %2 ==1:
          print(sayı **2)
# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
for sehir in sehirler:
     if (len(sehir)<=5):
          print(sehir)
# 5- Ürünlerin fiyatları toplamı nedir ? 
urunler = [
     {'name': 'samsung S6', 'price':'3000'},
     {'name': 'samsung S7', 'price':'4000'},
     {'name': 'samsung S8', 'price':'5000'},
     {'name': 'samsung S9', 'price':'6000'},
     {'name': 'samsung S10','price':'7000'}
]
toplam = 0
for urun in urunler:
     fiyat = int(urun['price'])
     toplam += fiyat
print('toplam fiyat:', toplam)
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
for urun in urunler:
     if (int(urun['price'])<=5000):
          print(urun['name'])
