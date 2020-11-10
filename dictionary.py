# Dictionary metodu ;
# key - value şeklinde çalışır.

# 34 => istanbul  
# 35 => izmir
"Önemli : List şeklinde yazıldığında :"
# Dictionary bilgisini kullanmadan liste olarak yazarsak;
sehirler = ['istanbul','izmir']
plakalar = [34,35]

# Plakalar içindeki 0.indeksi bulmak istersek şu metod uygulanır. 
print(plakalar[sehirler.index('istanbul')])  #yazılması gerekir.
print(plakalar[sehirler.index('izmir')])

# print(plakalar[sehirler.index('istanbul')]) # Bizi 34 bilgisine götürecektir.
# print(plakalar[sehirler.index('izmir')])  # Bizi 35 bilgisine ulaştıracaktır.

"Önemli : Dictionary bilgisiyle yazdırmak istersek : "
plakalar = { 'key' : 'value' }
plakalar = { 'istanbul' : '34', 'izmir' : 35 }
print(plakalar['istanbul'])
print(plakalar['izmir'])

plakalar['ankara'] = 6
print(plakalar)   # Bu durumda 'ankara' : 6 bilgisi eklenmiş olur.

plakalar['ankara'] = 'new value'
print(plakalar)   # Bu durumda plakalar içinde bulunan eleman 6 dan new value olarak değişir.

# ÖNEMLİ : Dictionary elemanlarına yenileri eklenebilir varolan elemanlar için de değişim gerçekleştirebilir.

# Başka bir örnekle devam edelim.

# users = {
#      'sinemcan': 24,
#      'uygarcan': 12,

# }

# print(users['uygarcan'])  # dediğimizde 'uygarcan' bilgisindeki 12 yazılacaktır.
# print(users['sinemcan']) 
# Böyle bir durumda sadece yaş bilgisi değil de örneğin 'sinemcan' metodu birçok bilgiye beni götürmeli.
# Bunun için aşağıdaki gibi yazdıralım.

users = {
     'sinemcan': {
      'age': 24,
      'roles': ['user'],
      'email': 'sinem@gmail.com',
      'adress': 'ankara',
      'phone': '523135161'

     },
     'uygarcan': {
      'age': 12,
      'roles': ['admin', 'user'],
      'email': 'uygar@gmail.com',
      'adress': 'ankara',
      'phone': '523135161'
     }
}     

# print(users['sinemcan'])
# print(users['uygarcan'])
# # Alt bilgileri yazmak istersek ; 
# print(users['sinemcan']['age'])
# print(users['uygarcan']['email'])

print(users['uygarcan'])
print(users['uygarcan']['roles'])
print(users['uygarcan']['roles'][0])



