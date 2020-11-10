x, y, z = (5, 10, 20)

# x, y = y, x  # x yerine y, y yerinde x değeri yazılır. Bu durumda sonuç : 10 5 20 olur.


# x = x + 5    # x in varolan değeriyle 5 toplanır sonuç : 10 olur. 10,10,20 şeklinde yazılır.


# x += 5 # yazdığımızda da yukardaki işlemin aynısını yapmış oluruz.
# x = 10 gelir yine.
# x -= 5 # yazdığımızda sonuç 5 olur. Bir önceki işlemde x = 10 olduğu için 10-5 ten sonuç 5 gelir.


# x *= 5 


# x /= 5 


# x %= 5


values = 1, 2, 3
print(values)
print(type(values))

x,y,z = values


x, y, z = values
values = 1,2 
# z ye karşılık gelen bir değer olmadığından sistem error verir.

values = 1, 2, 3, 4, 5
x, y, *z = values
# Bu şekilde yaptığımızda fazla olan 4 ve 5 değerleri de z nin içine yazılır.Z için bir liste oluşturulur.
print(x, y, z[0])
print(x, y, z[1])  # Z elemanı bir dizi, bir liste şeklinde yazılmıştır.

print(x,y,z)




