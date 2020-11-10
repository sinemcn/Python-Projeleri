# Eğer while döngüsünü kullanarak 0'dan 100'e kadar yazmak istersek;
# x = 0
# wihile True:
#      print(x) dersek: Duracağı bir yer bildirmediğimiz için sonsuza kadar 0 yazılır.

# Eğer while döngüsü x<100 için döndürmek istersek; Sistem 99 a kadar yazar ve her seferinde başa döner.
# Tekrar tekrar 99 a kadar yazar.
# while x<100:
     # print(x)


# ANCAK;
# Biz while döngüsünden çıkarmak için x'i 1 arttırarak 100 e kadar yazdırırsak sistem duracağı yeri
# algılar ve 100 e kadar yazıp durur.
x = 1
while x <=100:
     print(x)
     x+=1 
print('bitti...')

# Eğer 1'den 100'e kadar olan çift sayıları yazdırmak istersek;
x = 1
while x <=100:
     if (x %2 ==0):
          print(x)
     x+=1
print('bitti...')

# Eğer 1'den 100'e kadar olan tek sayıları yazdırmak istersek;
x = 1
while x <=100:
     if (x %2 ==1):
          print(x)
     x+=1
print('bitti...')

# 2- Hem çift, hem de tek sayıları yazdırmak istersek ve tek, çift şeklinde yanına yazarsak;
x = 1
while x<=100:
     if (x %2 == 0):
          print(f'sayı çift: {x}')
     else:
          print(f'sayı tek: {x}')
     x+=1
print('bitti...')

# 3- Başka bir örnek yaparsak;
name = ''  # Böyle bir değer tanımlaması bize #False yanıtını verir.

while not name:
     name = input('isminiz: ')
print(f'merhaba',name)

# Sistemi çalıştırdığımızda isim yazmadan sürekli enter a basarsak hiç değer yazılmaz. 
# isminiz: 
# isminiz: 
# isminiz: şeklinde yazmaya devam eder.
# Sistemde 'space' tuşuna basıp enter dersek sadece 'Merhaba' yazar.
name = ''
while not name.strip():
     name = input('isminiz: ')
print(f'merhaba,{name}')

# Bu işlem yapıldığı zaman space yapmak işe yaramaz. Strip metodu boşlukları yok eder ve isminiz: bölümüne 
# değer yazmamızı ister.