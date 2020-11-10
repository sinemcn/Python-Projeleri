list = [1, 2, 3]
tuple = (1, 'iki', 3)
print(type(list))
print(type(tuple))

print(tuple[2])  # Listede nasıl indeks sayısıyla karaktere ulaşılıyorsa tuple'da da bu işlem yapılır.
# Sonuç : 3 çıkacaktır.
# Eleman sayılarını yazdırmak içinde len metodunu kullanabiliriz.
print(len(tuple))  # Sonuç : 3 çıkacaktır.

# *** ÖNEMLİ *** : Bir liste içinde indeks sayısı hesaplanabilir ve indeks sayısı başka bir elemana eşitlenerek değiştirilebilir!
# *** ÖNEMLİ *** : TUPLE da indeks sayısı hesaplanabilir ama o indeks sayısı başka bir değerle DEĞİŞTİRİLEMEZ!
# *** ÖNEMLİ *** : TUPLE ile LİSTE arasındaki fark karakter değişimi yapılamamasıdır.
tuple = ('damla', 'ayşe')
tuple = tuple.count('ayşe')
print(tuple)  # Count metodu tuple kullanılır.

tuple = ('damla', 'ayşe')
tuple = tuple.index('ayşe')
print(tuple)  # Index metodu tuple da kullanılır.

names = ('demet', 'emel', 'ayşe')
tuple = ('damla', 'ayşe', 'ayşe')
names = ('demet', 'emel', 'ayşe') + tuple
print(names)  # Bu durumda names ve tuple karakterleri tek bir liste halinde yazılır.

# *** LİSTE VE TUPLE ARASINDAKİ TEK FARK HERHANGİ BİR SİLME YA DA GÜNCELLEME İŞLEMİ YAPILAMAMASIDIR.


