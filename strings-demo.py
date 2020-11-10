website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
lenght = len(website)

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[lenght-3:lenght]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
result = course[:15]
result = course[-15:-1]
result = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::]   # Bu ifade baştan sona yazma ifadesidir. # Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat) aynen yazılır.
result = course[::1]  # Buraya 1 değerini yazarsam ifade aynen gelir.
result = course[::2]  # Buraya 2 yazarsam adım sayısı belirtmiş olurum ve karakterleri 2 adımda bir alır.
result = course[::3]  # Buraya 3 yazarsak karakterleri 3 adımda bir alır.

# 'course' ifadesindeki karakterleri tersten yazdırmak için şu işlem yapılır!

result = course[::-1] # İfadelerin hepsi :: şeklinde seçilir ve tersten istendiği için [::-1] yazılır!   

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

print('Benim adım {} {} yaşım {} ve mesleğim {}.'.format(name, surname, age, job))


# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
result = s[6]
s = s[0:6] + 'W'+ s[-4:]
print(s)
# Kısa yol sonradan öğrenicez.
s = s.replace('w', 'W')

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

# Hoca bu şekilde yazdı.
result = 'abc' * 3  #abcabcabc yazılır. 
# Boşluk bırakmak istersek 
result = 'abc ' * 3   # şeklinde yazılır.


print(result)