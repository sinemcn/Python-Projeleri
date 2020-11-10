name = 'Sinem Can'

for letters in name:
     print(letters)  # Bu şekilde tüm harfleri yazdırırım.

# ANCAK; Tüm harfleri yazdırmak istemezsem if bloğu yazarak break ile döngüyü durdururum.

for letters in name:
     if letters == 'a':
          break
     print(letters)   # Sistem 'a' harfine geldiği anda durur. 'a' dan önce olan tüm karakterler yazılır.
# Sonuç olarak; Sinem C yazdırılır.

# Eğer break değil de continue kullanırsak bu durumda if bloğunda tanımlanan karakter atlanır, 
# diğer tüm karakterler yazdırılır.

for letters in name:
     if letters == 'a':
          continue
     print(letters)
# Sonuç olarak Sinem Cn yazdırılır.

# WHILE DÖNGÜSÜ ÜZERİNDE BİR ÖRNEK YAPALIM.
x = 0
while x < 5:
     print(x)
     x+=1
# Eğer bunu yazdırırsak 0'dan 4'e kadar olan sayılar yazdırılır.
x = 0
while x < 5:
     if x == 3:
          break
     print(x)
     x+=1
# Bu durumda 3'e kadar yazar ve sistem durdurulur.3 yazılmaz!

x = 0
while x < 5:
     x+=1
     if x == 2:
          continue
     print(x)
# Bu durumda sadece 2 atlanır, yazılmaz. Diğer tüm elemanlar yazılır.

# ÖRNEK YAPALIM :
# 1-100'e kadar olan tüm sayıların toplamı nedir?
x = 1
result = 0
while x<=100:
     result += x
     x+=1
print(f'toplam: {result}')
# Bu durumda sonuç: 5050 gelecektir.

# 1-100'e kadar tek sayıların toplamı nedir ?
x = 1
result = 0
while x <= 100:
     x+=1
     if x % 2 == 1:
          continue
     result += x
print(f'toplam: {result}')
# Bu durumda sonuç : 2550 çıkacaktır.

x = 1
result = 0
while x <= 100:
     x+=1
     if x % 2 == 0:
          continue
     result += x
print(f'toplam: {result}')
# Bu durumda sonuç : 2600 çıkacaktır.
