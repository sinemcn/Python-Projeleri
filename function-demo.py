# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def yazdir(kelime, adet):
     print(kelime * adet)
yazdir('Merhaba', 10)   # Bu durumda sistem 10 kere merhaba yazar.
yazdir('Merhaba\n', 10) # Bu durumda sistem 10 kere aşağı doğru merhaba yazdırır.

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon oluşturun.

def listeyeCevir(*params):  # (*) kullandığımız bu işaret sınırsız sayıda parametre alabileceğimizi gösterir !
     liste = []

     for param in params:
          liste.append(param)

     return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalSayılariBul(sayi1, sayi2):
     for sayi in range(sayi1, sayi2+1): # sayi2 yi alabilmek için sayi2 ye 1 eklenir. sayi2+1 şeklinde yazılır.
          if sayi > 1:
               for i in range(2, sayi):
                    if (sayi % i == 0):
                         break
               else:
                    print(sayi)

sayi1= int(input('sayı 1: '))
sayi2= int(input('sayı 2: '))   

asalSayılariBul(sayi1, sayi2)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

def tamBolenleriBul(sayi):
     tamBolenler = []

     for i in range(2, sayi):
          if (sayi % i == 0):
               tamBolenler.append(i)
     return tamBolenler

print(tamBolenleriBul(20))
print(tamBolenleriBul(300))    # Sonuç: [2, 4, 5, 10]  çıkar !
