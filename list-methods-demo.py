names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
print(names)
# 3- "Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)
names.pop(-1)
print(names)
# 4- "Deniz" isminin indeksi nedir? 
names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
index = names.index('Deniz')
print(index)
# 5- "Ali" listenin bir elemanı mıdır?
result = 'Ali' in names
print(result)
# 6- Liste elemanlarını ters çeviriniz.
names.reverse()
print(names)
# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)
# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)
# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)
# 10- years dizisinin en büyük ve en küçük elemanı nedir?
min = min(years)
print(min)
max = max(years)
print(max)
# 11- years dizisinde kaç tane 1998 değeri vardır? 
years = [1998, 2000, 1998, 1987]
years = years.count(1998)
print(years)
# 12- years dizisinin tüm elemanlarını siliniz.
years = [1998, 2000, 1998, 1987]
years.clear()
print()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka: ")  # Bizden 3 marka bilgisi istediği için 3 kere yazarız.
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)  # Bu işlem sonunda tanımlanan her marka liste içine string bir değer olarak yazılacaktır.
