# Bu uygulamada bir veri yapımız olacak. (Dictionary kapsamında)

SinemHesap = {             
     'ad': 'Sinem Can',        
     'hesapNo': '13245678',      
     'bakiye': 3000,             
     'ekHesap': 2000             
}

UygarHesap = {
     'ad' : 'Uygar Can',
     'hesapNo' : '12345678',
     'bakiye' : 2000,
     'ekHesap' : 1000
}

# Örneğin 2 kişinin hesabı olacak.Bu bilgi objelerini parametre olarak alıp
# yine bu veri yapıları üzerinden para çekme işlemleri yapmayı denicez.
# Örneğin: Hesabımdan 2000 tl çekmeyi istiyorum,eğer yetiyorsa bana bu
# parayı verir.Eğer yetmiyorsa ek hesabı kullanmaya çalışacak.Eğer ek hesap-
# ta para yeterliyse verir.Eğer değilse bakiye yeter diyecek.


# Bir fonksiyon tanımlayalım.
# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")
# paraCek(SinemHesap,2000)
# Sonuç olarak : Merhaba Sinem Can yazar.

# Para çekme işlemlerimizi yerine getirelim.

# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")

#      if (hesap['bakiye'] >= miktar):
#           print(f'Paranızı alabilirsiniz.')
#      else:
#           toplam = hesap['bakiye'] + hesap['ekHesap']

#           if (toplam >= miktar):
#                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')
               
#                if ekHesapKullanimi == 'e':
#                     print('Paranızı alabilirsiniz.')
#                else:
#                     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")
#           else:
#                print('Üzgünüz bakiye yetersiz.')

# paraCek(SinemHesap,3000)
# Sonuç : 
# Merhaba Sinem Can 
# Paranızı alabilirsiniz.   şeklinde gelecektir.

# Eğer paraCek(SinemHesap,9000) yazarsam sistem sonuç olarak;
# Merhaba Sinem Can 
# Üzgünüz bakiye yetersiz  şeklinde cevap verecektir.

# Eğer paraCek(SinemHesap,4000) yazarsam sistem sonuç olarak;
# Merhaba Sinem Can 
# Ek hesap kullanılsın mı (e/h):    sorusunu yöneltecek ve cevap olarak e girersem
# Paranızı alabilirsiniz.   yazacaktır.

# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")

#      if (hesap['bakiye'] >= miktar):
#           print(f'Paranızı alabilirsiniz.')
#      else:
#           toplam = hesap['bakiye'] + hesap['ekHesap']

#           if (toplam >= miktar):
#                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')
               
#                if ekHesapKullanimi == 'e':
#                     print('Paranızı alabilirsiniz.')
#                else:
#                     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")
#           else:
#                print('Üzgünüz bakiye yetersiz.')

# paraCek(SinemHesap,4000)   

# Bu durumda sistem 
# Merhaba Sinem Can 
# Ek hesap kullanılsın mı (e/h):   diye sorar ve h yanıtını girersem cevap olarak hesabımda ne kadar olduğunu yazar.
# 13245678 nolu hesabınızda 3000 vardır.  şeklinde yanıt verecektir.


# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")

#      if (hesap['bakiye'] >= miktar):
#           print(f'Paranızı alabilirsiniz.')
#      else:
#           toplam = hesap['bakiye'] + hesap['ekHesap']

#           if (toplam >= miktar):
#                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')
               
#                if ekHesapKullanimi == 'e':
#                     print('Paranızı alabilirsiniz.')
#                else:
#                     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")
#           else:
#                print('Üzgünüz bakiye yetersiz.')

# paraCek(SinemHesap,5100)

# Eğer sisteme hesap ve ekHesap toplamından fazla bir miktar girersem ve çekmek istersem, sistem 
# Üzgünüz yetersiz bakiye yazacaktır.


# Eğer hesaptan para çekip 2.kere para çekmek istersek; miktar değişeceğinden hesaptaki para miktarında 
# değişiklik yapmamız gerekir.

# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")

#      if (hesap['bakiye'] >= miktar):
#           hesap['bakiye']-= miktar
#           print('Paranızı alabilirsiniz.')
#      else:
#           toplam = hesap['bakiye'] + hesap['ekHesap']

#           if (toplam >= miktar):
#                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')

#                if ekHesapKullanimi == 'e':
#                     print('Paranızı alabilirsiniz.')
#                else:
#                     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")

#           else:
#                print('Üzgünüz bakiye yetersiz.')

# paraCek(SinemHesap,3000)
# paraCek(SinemHesap,3000) 

# Ek hesaptaki para çekimi sonrası bakiyeyi güncelleme işlemi şöyle yapılır.

# def paraCek(hesap,miktar):
#      print(f"Merhaba {hesap['ad']}")

#      if (hesap['bakiye'] >= miktar):
#           hesap['bakiye']-= miktar
#           print('Paranızı alabilirsiniz.')
#      else:
#           toplam = hesap['bakiye']+hesap['ekHesap']

#           if (toplam >= miktar):
#                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')
#                if ekHesapKullanimi == 'e':
#                     ekHesapKullanilacakMiktar = miktar-hesap['bakiye']
#                     hesap['bakiye']=0
#                     hesap['ekHesap']-=ekHesapKullanilacakMiktar
#                     print('Paranızı alabilirsiniz')
#                else:
#                     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")
#           else:
#                print('Üzgünüz bakiye yetersiz.')

# paraCek(SinemHesap,3000)
# paraCek(SinemHesap,3000)  
# # Sonuç : Merhaba Sinem Can 
# # Paranızı alabilirsiniz.
# # Merhaba Sinem Can 
# # Üzgünüz bakiye yetersiz.

# paraCek(SinemHesap,3000)
# paraCek(SinemHesap,2000)
# Sonuç : Merhaba Sinem Can
# Ek hesap kullanılsın mı (e/h):e dersek;
# Paranızı alabilirsiniz.    yazacaktır.


# Burada dikkat etmemiz gereken yerler;
# Bizim dictionary şeklinde tanımlamış olduğumuz dışarıdaki objeler bilgisayarımızda,ram içinde reference type 
# olarak ele alınıyor.Bunların bir referansı tutuluyor.Ben bu referansları bir metoda,fonksiyona gönderdiğimde
# bu bilginin adresi gönderiliyor.Bu obje üzerinde fonk.içerisinde bir güncelleme yaptığımız zaman(örneğin;
# bakiye bilgisi) DIŞARIDAKİ BİLGİLER üzerinde de güncelleme yapılıyor.Çünkü aynı adresteki, aynı veriyi 
# güncellemiş oluyorum.

# EĞER ;
# ad = 'Ali'
# hesapNo: '1234456'
# bakiye = 3000      şeklinde bir değişkene eşitleseydik aşağıda yazacağımız fonksiyonun içinde herhangi bir
#                    güncelleme yaptığımızda yukarıdaki bilgi GÜNCELLENMEZDİ !

# Gönderilen parametre bir obje değilse (dictionary = {}) normal bir değişken yapısıysa (ad='ali') bu durumda
# fonksiyon içerisinde bir kopyalama işlemi yapılır.

# Bankamatik hesabı olarak tanımladığımız fonksiyonun en sonunda hesap ve ekhesap'ta ne kadar para kaldığını 
# para çekme işleminden sonra yazdırmak istersek; bir tane daha fonksiyon yazarız.

def paraCek(hesap,miktar):
     print(f"Merhaba {hesap['ad']}")

     if (hesap['bakiye']>=miktar):
          hesap['bakiye']-=miktar
          print('Paranızı alabilirsiniz.')
     else:
          toplam = hesap['bakiye']+hesap['ekHesap']

          if (toplam >= miktar):
               ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h):')
               if ekHesapKullanimi == 'e':
                    ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                    hesap['bakiye'] = 0
                    hesap['ekHesap']-= ekHesapKullanilacakMiktar
                    print('Paranızı alabilirsiniz.')
               else:
                    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")

          else:
               print('Üzgünüz bakiye yetersiz.')

def bakiyeSorgula(hesap):
     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL vardır.Ek hesapta {hesap['ekHesap']} TL vardır.")

paraCek(SinemHesap,3000)
bakiyeSorgula(SinemHesap)
print('*****************************************************************')

paraCek(SinemHesap,4000)
bakiyeSorgula(SinemHesap)
print('*****************************************************************')

paraCek(SinemHesap,2000)
bakiyeSorgula(SinemHesap)