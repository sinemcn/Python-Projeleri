# ERROR TÜRLERİ

# print(a) => NameError: Tanımlanmamış bir değişken.
# int('1a2') => ValueError: Sadece sayısal ifade girilmesi gerekir.
# print(10/0) => ZeroDivisionError: 0'a bölünemez hatası verir.
# print('denem'e) => SyntaxError: Yanlış bir ifade yazdık.


# Bu hata türleri dışında birçok hata türü vardır.Bu hata türlerine python.org => Exception hierarchy 
# bölümünden ulaşabiliriz.

# ERROR HANDLING 

# ZeroDivisionError 
# x ve ye değişkeni tanımlayalım.

x = int(input('x: '))
y = int(input('y: '))
print(x/y)
# Sonuç olarak: ZeroDivisionError: division by zero  hatası alırız.

