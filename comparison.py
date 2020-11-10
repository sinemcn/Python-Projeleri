# username, password verilir ve sisteme database olarak bilgiler kayıt edilir.
# Kullanıcı sisteme girdiğinde username: 'sinemcan', password: 123456 şeklinde yazarız.
# Bu bilgiler doğruysa sözkonusu kullanıcı gitmek istediği alana yönlendirilir.

a, b, c, d = 5, 5, 10, 4 
# a==b => dediğimizde a değeri b ye eşit mi diye sorarız. Eğer a ve b değerleri eşitse sonuç True çıkacaktır.

result = (a == b) 
result = (a == c)

password = '12345'
username = 'sadikturan'
result = ('sdktrn' == username)
result = ('sadikturan' == username)
result = (a != b) # Burada a, b'ye eşit değil mi diye sorarız. Cevap: False olur. a değeri b'ye eşittir.
result = (a != c) # a, c'ye eşit değil mi diye sorduğumuzda Cevap: True olur. a değeri c' ye eşit değildir.
result = (a > b)  # a, b'den büyük müdür ? sorusunun cevabını ararız. Cevap: False olur. Çünkü eşittir.
result = (a < c)  # a, c'den küçük müdür ? sorusunun cevabı True olur.
result = (a >= b) # Bu durumda True cevabı gelecektir.Çünkü büyük değil ancak eşittir.
result = (a <= b) # Bu durumda True cevabı gelecektir.Çünkü küçük değil ancak eşittir.
result = (c <= b) # Bu durumda cevap False gelecektir.Çünkü hem küçük değil hem de eşit değildir.
result = (True == 1) # Cevap True gelecektir.Çünkü True değeri numeric olarak 1'e eşittir.
result = (False == 0) # Cevap True gelecektir.Çünkü False değeri numeric olarak 0'a eşittir.
result = (True + False + 40) # dersek ve bunu yazdırırsak => Cevap : 41 gelecektir.

print(result)
