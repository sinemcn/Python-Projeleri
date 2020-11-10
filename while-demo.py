# 1- sayilar listesini ekrana yazdırınız.
sayilar = [1,3,5,7,9,12,19,21]
x = 0
while x<(len(sayilar)):
     print(sayilar[x])
     x +=1     

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları
# ekrana yazdırın.
baslangıc = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangıc
while i < bitis:
     i+=1
     if (i %2==1):
          print(i)
    

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
x = 100
while x > 0:
     print(x)
     x-=1



# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []

i = 0

while i<5:
     sayi = int(input('sayı: '))
     numbers.append(sayi)
     i+=1
numbers.sort()
print(numbers)

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name,price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeyin.

urunler = []

adet = int(input('kaç adet ürün eklemek istersiniz: '))
i = 0

while (i<adet):
     name = input('ürün adı: ')
     price = input('ürün fiyatı: ')
     urunler.append({
          'name': name,
          'price': price
     })
     i += 1
for urun in urunler:
     print(f'ürün adı: {urun["name"]} - ürün fiyatı: {urun["price"]}')

