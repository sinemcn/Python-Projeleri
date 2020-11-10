def sayHello():
     print('Hello')

sayHello()
sayHello()
sayHello()

def sayHello():
     print('Hello user')
sayHello()

def sayHello(name = 'user'):
     print('Hello '+name)
sayHello('Sinem')
sayHello('Uygar')
sayHello()  # Bu şekilde bırakıp herhangi bir parametre göndermezsek direk user yazılır ! name = user dedik.

# Eğer sistemi geriye döndürmek istersek ve print ile yazdırmazsak; return kullanılır !

def sayHello(name = 'Sinem'):
     return 'Hello '+ name

msg = sayHello('Sinem')
msg = sayHello('Uygar')
print(msg)
# Msg değişkeninin içine atama yapar ve yazdırırım.
# msg'nin içine en son hangi değer tanımlanırsa o yazdırılır.

def total(num1, num2):
     return num1 + num2
result = total(10,20) # sonuç : 30 
result = total(15,20) # Bu result değerini yazdırdığımızda sadece 35 yazar.
print(result)  # Total değişkeninin içindeki değerler değiştirilebilir.

def yasHesapla(dogumYili):
     return 2020 - dogumYili

ageSinem = yasHesapla(1996)
ageGizem = yasHesapla(1997)
ageUygar = yasHesapla(2008)

print(ageSinem)
print(ageGizem)
print(ageUygar)

def EmekliligeKacYilKaldi(dogumYili, isim):
     yas = yasHesapla(dogumYili)
     emeklilik = 52 - yas

     if emeklilik > 0:
          print(f'Emekliliğinize {emeklilik} yıl kaldı.')
     else:
          print('Zaten emeklisiniz.')
EmekliligeKacYilKaldi(1996, 'Sinem')
EmekliligeKacYilKaldi(1966, 'Oktay')
EmekliligeKacYilKaldi(1970, 'Emine')





