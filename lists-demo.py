# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste kaç elemanlıdır ? 

result =len(arabalar)
print(result)
# 3- Listenin ilk ve son elemanı nedir? 
result = arabalar[0]  # Arabalar listesinin ilk elemanı [0] olan Bmw dir.
print(result)
result = arabalar[3]
print(result)
result = arabalar[-1] # Mazda bizim için en string olacağından son elemanı bulmak için [-1] de kullanabiliriz.
print(result)

# 4- Mazda değerini Toyota ile değiştirin.
# arabalar[-1] = 'Toyota'
# result = arabalar
# print(result)
# 5- Mercedes listenin bir elemanı mıdır ? 
result = 'Mercedes' in arabalar # Burada listenin içinde mercedes olduğu için cevap True çıkacaktır.
print(result)
# 6- listenin -2 indeksindeki değer nedir?
result  = arabalar[-2]
print(result)
# 7- Listenin ilk 3 elemanını alın.
result = arabalar[0:3]
print(result)
# 8-Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota', 'Renault']
result = arabalar
print(result)
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ['Audi', 'Nissan']
print(result)
# 10-Listenin son elemanını silin.
del arabalar[-1]
result = arabalar
print(result)
# 11-Liste elemanlarını tersten yazdırın.
result = arabalar[::-1]
print(result)
# 12-Aşağıdaki verileri bir liste içinde saklayınız.

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet','Turan', 1998, [80,70,90]]
students = studentA + studentB + studentC

print(students)

# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
print(result)
result = studentB[1]
print(result)
result = studentC[3][1]
print(result)

result = f"Yiğit Bilgi 9 yaşında ve not ortalaması 66" # Bilgisini yazdırmak istersek.
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)

# Not ortalamasındaki tam sayıdan sonraki kısımları silin.
results = (studentA[3][0] + studentA[3][1] + studentA[3][2])/3
print('{r:1.3}'.format(r = results))


