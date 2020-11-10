numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
print(val)
val = max(numbers)
print(val)

val = min(letters)  # Alfabetik sıralamaya göre yazılır.
print(val)
val = max(letters)
print(val)

val = numbers[3:6]  # Numbers içindeki karakterleri 3'ten 6 ya kadar yaz.
print(val)

val = numbers[:3]
print(val)

val = numbers[4:]
print(val)

numbers[4] = 40   # Numbers parametresine 4.indekste 40 yazmak istersek bu işlem yapılır. 4 yerine 40 yazılır.
print(numbers)

numbers.append(49)  # Append metotuyla listenin SONUNA parantez içine yazılan değer eklenir.
print(numbers)

numbers.insert(3, 78)  # Insert değerinde istediğimiz konuma eleman ekleyebiliriz. 3.indekse 78 eklediğimizde 16 bir sağa 4.indekse kayar.
print(numbers)

numbers.insert(-1, 52) # En sona 52 sayısı eklenir. Ancak en son değer 49 olduğu için 49 bir sağa kayacak ve 52, 49 dan önce yazılacaktır.
print(numbers)

# numbers.pop()  # Eleman silmek istediğimizde bunu kullanırız.
# print(numbers) # Bu durumda en sondaki sonradan append metoduyla eklenen 49 sayısı silinecektir.

# numbers.pop(0)
# print(numbers) # Dersek bu durumda sadece 0.indeks yani 1 sayısı silinmiş olacaktır.

# numbers.pop() ve numbers.pop(-1) aynı sonucu verecek olup listeye en son eklenen 49 değerini silecektir.

# numbers.remove(52)  # Bu metotta silmek istediğimiz karakteri veririz ve liste içinde silinmesi istenen karakter bulunur ve silinir.
# print(numbers)

numbers.sort()  # Bu metotta liste içinde verilen karakterler sayısal veya alfabetik olarak sırasıyla yazılacaktır.
print(numbers)
letters.sort()
print(letters)

numbers.reverse()  # Bu metotta liste içinde verilen karakterler sayısal ve alfabetik olarak tersten yazılır. Yani sayısal ve alfabetik olarak büyükten küçüğe doğru bir sıralama yapılır.
print(numbers)

# Len : Bu metotta listenin eleman sayısı bulunur.
print(len(numbers))
print(len(letters))

# Count : Bu metotta liste içinde bulunan bir değerin kaç tane olduğunu yazdırabiliriz.
letters = letters.count('s')
print(letters)
numbers = numbers.count(10)
print(numbers)

# Clear : Bu metotta listenin içindeki tüm karakterler silinir.
numbers = [1, 10, 5, 16, 4, 9, 10]
numbers.clear()
print(numbers)

letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
letters.clear()
print(letters)


