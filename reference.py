# Value Types => String, number metodlarında kullanılır.
x = 5
y = 25

x = y
y = 10
print(x, y)   # Sonuç : 25 10 olur.

# Reference Types => List ve class yapısında kullanılır. (Class'ı görmedik daha sonra geçicez.)
a = ["apple", "banana"]
b = ["apple", "banana"]
a = b 
b[0] = "grape"
print(a, b)    # Sonuç : ['grape', 'banana']['grape','banana] şeklinde yazılır. 
# a=b durumunda ikisi de aynı adresi taşır ! Bu yüzden birisinde yapılan değişiklik diğerinde de otomatik olarak yapılır.
# Liste içerisinde bir adres bilgisi taşınır.Veri içinde adres bilgisi ilişkilendirilir.Liste içinde eşitlenme durumunda adresler eşitlenir.İkisi de aynı adresi gösterir.
# *** Adres eşitlemesi yapıldığından hedef aynı seçilir.***

