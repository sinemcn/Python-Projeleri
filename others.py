# Identity Operator : is 
# is operatörü : Bu operatörde tanımlanan listelerin aynı olup olmadığı yani tanımlanan listelerin aynı adrese ait olup olmadığı incelenir.
# Eğer aynı adresteyse True değeri, eğer değilse False değeri gelecektir.

x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)  # Sonuç : True gelir. 
print(x == z)  # Sonuç : True gelir.
# Bu iki durumda x, y ve z birbirlerine eşit olduğundan True değeri gelecektir.
print(x is y)  # Bu durumda x ve y birbirine eşit olduğu için sonuç True gelir. Adresler aynıdır.
print(x is z)  # Bu durumda x ve z birbirine eşit olamdığı için sonuç FALSE gelecektir.

x = [1, 2, 3]
y = [2, 4]
print(x == y) # Liste içindeki elemanlar farklı olduğundan sonuç : False çıkacaktır.
print(x is y)  # Adresler farklı olduğundan sonuç : False gelir.

# Eğer x ve y'i birbirine benzetmek istersek ;
del x[2]
y[1] = 1
y.reverse()
print(x)  # Sonuç : [1, 2]  gelecektir.
print(y)  # Sonuç : [1, 2]  gelecektir.
print( x == y)  # Bu durumda x ve y aynı elemanlara sahip olduğundan sonuç : TRUE gelir.
print(x is y)   # Bu durumda adresler farklı olduğu için sonuç : FALSE gelir.
print(x is not y) # Bu durumda sonuç : TRUE çıkar.


# in Operator : in

x = ['apple', 'banana']
print('banana' in x)  # True bilgisi gelecektir.

name = 'Çınar'
print('a' in name) # TRUE 
print('s' in name) # FALSE olur.
print('a' not in name) # FALSE gelir.
