# def square(num): return num ** 2

# result = square(3)
# print(result) 



def square(num): return num ** 2 

numbers = [1,3,5,9]

result = list(map(square, numbers))  # Sonuç: [1, 9, 25, 81] şeklinde gelecektir. Burada list şeklinde yazmak zorundayız.
                                     # Yoksa sistem error verir. Map'ten dönen sonuç listeye çevrilir.
print(result) 

# Bu işlemin alternatifi olarak da for döngüsü kullanabiliriz.

for item in map(square, numbers):
     print(item)   # Bu işlemi yaptığımızda da sistem liste elemanlarını alt alta yazar. Karelerini alır.

# Sonuç : 
# 1
# 9
# 25
# 81

numbers = [1,3,5,9]

result = list(map(lambda num: num ** 2, numbers ))
print(result)   # Sonuç : [1, 9, 25, 81] şeklinde yazılır.

# Bu işlemi lambda ile de yaparız. Yani isimsiz bir fonksiyonla yapmış olurum.
# Yaptığımız işleme bir isim de verebiliriz.

square = lambda num : num ** 2       # şeklinde yazabiliriz.
result = list(map(square, numbers))  # yazar ve print ile yazdırırsak yine aynı sonuca ulaşmış oluruz.
result = square(3)  # şeklinde de yazabiliriz. Bu şekilde de direk sonuca ulaşılır.
print(result)

# Eğer liste içinde yazan elemanların sadece ÇİFTLERİNİ GERİYE DÖNDÜRMEK istersem; FILTER fonksiyonu kullanırım.
# Öncelikle normal bir fonksiyon tanımlaması yapalım daha sonra lambda'ya çevirelim.

# numbers = [1,3,5,9,10,4]              
# def check_even(num): return num %2 ==0 

# result = list(filter(check_even,numbers))     
# print(result)
# SONUÇ : [10,4] çıkacaktır.

# Eğer lambda kullanmak istersek ;
numbers = [1,3,5,9,10,4]
def check_even(num): return num % 2 == 0

result = list(filter(lambda num: num %2 == 0, numbers))
print(result)      # SONUÇ : Yine [10,4] çıkacaktır ! 

# check_even ' ı lambdya eşitlersek ;
check_even = lambda num: num % 2 == 0
result = list(filter(check_even,numbers))
print(result)     # Sonuç : Yine [10,4]  gelir.

result = check_even(numbers[2])
print(result)     # Sonuç : FALSE gelecektir. Çünkü 2.indeksteki sayı çift değildir.