website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
print(result)


# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print(result)


# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
print(result)
lenght =len(website)
result = website[lenght-3:lenght]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
print(result)
result = course[:15]
print(result)   # İki durumda aynı sonucu verecektir.
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print(result)    # Bu durumda course karakteri tersten yazılır.
# (Sonuç: taas 04( zinirebheR amalmargorP nohtyP anoS natşaB :usruK nohtyP ) Olacaktır !


name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
print('Benim adım {} {} , yaşım {} ve mesleğim {}.'.format(name, surname, age, job))

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s.replace('w', 'W')
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc' * 3   # Bu şekilde yazarsak sonuç abcabcabc olarak yazılacaktır.
print(result)
result = 'abc ' * 3  # Bu şekilde yazarsak sonuç abc abc abc olarak yazılacaktır.
print(result)



