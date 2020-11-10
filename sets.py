fruits = {'orange', 'apple', 'banana'}
# print(fruits)  # Yazdırma işlemi yapıldığında liste içindeki elemanlar karışık yazılır.

# Elemanlar yazdırıldığında YERLERİ KARIŞIK olarak yazılacağı için indeks sayılarıyla eleman BULUNAMAZ !
# Sistem ERROR verir ! İNDEKSLENEMEZ !

# Elemanlar herhangi bir sayısal büyüklük - küçüklük ya da alfabetik sıralamaya göre sıralanamaz !
# sort reverse kullanılamaz !

# *** Sadece şu şekilde sıralanabilir. ( Döngü olarak => sonra görücez bu konuyu)
fruits = {'orange', 'apple', 'banana'}
for x in fruits:
     print(x)    # Bu şekilde döngü yoluyla ulaşılabilir. Sonuç : orange, apple, banana şeklinde yazılır.

# Listeye yeni bir eleman eklemek istersek add metodunu kullanabiliriz.
fruits.add('cherry')
print(fruits)  # {'cherry', 'apple', 'banana', 'orange'}  şeklinde cherry listeye eklenmiş olur.

# Aynı şekilde update metoduyla da başka bir liste içindeki elemanları fruits listesine ekleyebiliriz.
# Update metoduyla birbirinden bağımsız iki liste birleştirilebilir.

fruits.update(['mango','grape'])
print(fruits)   # {'cherry', 'banana', 'apple', 'grape', 'mango', 'orange'} şeklinde yazılmış olacaktır.
# Böylelikle iki farklı listenin birleştirildiğini görürüz.

# Liste içinde olan bir eleman tekrardan yazılmak istenirse listede önceden olduğu için iki kere yazılmaz !
fruits.update(['mango','grape','apple'])
print(fruits)   # {'orange', 'cherry', 'apple', 'grape', 'mango', 'banana'} yine bu şekilde tek seferde yazılır.

myList = [1,2,5,4,4,2,1]
print(myList)  # Listedeki elemanlar aynen yazılır.

# Set metoduyla yazarsak liste içindeki tekrarlayan elemanlar tek seferde yazılır.
print(set(myList))  # {1, 2, 4, 5} sonuç bu şekilde gelecektir.

# Listeden eleman silmek istediğimizde :
fruits.remove('apple')
print(fruits)  # {'banana', 'cherry', 'mango', 'orange', 'grape'} sonuç olarak yazılır.Apple silinir.

# Discard metoduyla da istenilen eleman silinebilir.
fruits.discard('mango')
print(fruits)   # {'orange', 'grape', 'cherry', 'banana'} bu durumda mango da silinir.

# POP METODU YAZILABİLİR AMA KULLANILMAZ !!! Bunun nedeni liste her yazdırıldığında elemanların yeri değişecek ve en son yazılan değer sürekli değişecektir.
# Bu durumda pop metodunu kullandığımızda her seferinde silinen eleman değişecektir.

# Clear metodu kullandığımızda tüm elemanlar silinir.
fruits.clear()
print(fruits)    # set() sonuç bu şekilde olacaktır.
















