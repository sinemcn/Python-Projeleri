# 1- Girilen 2 sayıdan hangisi büyüktür ?
a = int(input('a: '))
b = int(input('b: '))
result = (a > b)
print(f'a: {a} b: {b} den büyüktür: {result}')
# a değerine : 10 ve b değerine : 5 verirsek sonuç : True çıkacaktır.
# a değerine : 5 ve b değerine : 10 verirsek bu durumda sonuç : False çıkacaktır.

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı diye yazdırın.

vize1 = float(input('1.vize: '))
vize2 = float(input('2.vize: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f'not ortalamanız: {ortalama} ve dersi geçme durumunuz: {ortalama >=50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input('sayı: '))
tekcift = (sayi % 2 == 0)
print(f'girilen sayının çift olma durumu: {tekcift}')

# 4- Girilen bir sayının negatif veya pozitiflik durumunu yazın.

sayi = int(input('sayı: '))
pozitifmi = (sayi > 0)
print(f'girilen sayının pozitif olma durumu: {pozitifmi}')


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#     (email: email@sadikturan.com  parola: abc123)

email = 'email@sinem.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.strip())
isPassword = (password == girilenPassword.lower())
print(f'Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isPassword}')
