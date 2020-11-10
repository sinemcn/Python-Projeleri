website = 'http://www.sadikturan.com'
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '
result = result.strip()
print(result)
# Eğer sadece soldaki boşluğu silmek istersek result = result.lstrip()  (left = l)
# Eğer sadece sağdaki boşluğu silmek istersek result = result.rstrip()  (right = r)
result = ' Hello World '
result = result.lstrip()
print(result)

result = result.rstrip()
print(result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = website.lstrip('/:pth')  # Bu işlem website ın içindeki karakterin sol tarafını siler.
print(result)

# SADECE sadikturan bilgisine ulaşmak istersek şu yapılır !
result = website.strip(':/whtp.com')  # Çıkarılmak istenen karakterler yazılır.
print(result)  

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapınız.
result = course.lower()
print(result)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')      # Cevap: 2 olur.
print(result)

result  = website.count('www')   # Cevap: 1 olur.
print(result)

result = website.count('www',0,10)  # Bu durumda 0 ile 10 arasında www yazılmış mıdır onu buluruz.  # Cevap: 1 olur.
print(result)

# 5- 'website' www ile başlayıp com ile bitiyor mu ?
result = website.startswith('www')    # False 
print(result)   

result = website.endswith('com')        # True 
print(result)




# 6- 'website' içindeki '.com' ifadesi var mı ? 
result = website.find('.com')  # 21 indeks numarasıyla buluruz. 
print(result) 

result = website.find('com',0,10)  # '.com' karakteri 0 ile 10 indeks sayıları arasından var mıdır ona bakarız !
print(result)   # Cevap -1 olacaktır. Çünkü 0 ve 10 indeks sayıları arasında .com karakteri yazılı değildir.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
isalpha = course.isalpha()  # isalpha course karakterlerinin alfabetik mi diye sorar. Cevap: False olacaktır. Sayısal değer de vardır.(40 saat)
print(isalpha)


isdigit = course.isdigit()  # Gelen değerler rakam mı diye sorulur.
print(isdigit)              # Cevap: False olacaktır.

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*')
print(result)
result = 'Contents'.ljust(50, '*')
print(result)
result = 'Contents'.rjust(50, '*')
print(result)
# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ','-')
print(result)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
result = 'Hello World'
result = 'Hello World'.replace('World', 'There')
print(result)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split()
print(result)
print(result[3])