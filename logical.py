x = 5 
result = 5 < x < 10  # Sonuç : False çıkar 

# x = 6 
# result = 5 < x < 10 

# And Operatörü 
result = (x > 5) and (x < 10)

hak = 5 
devam = 'e'
result = (hak > 0) and (devam == 'e')  # Sonuç : True olur.

hak = 0
devam = 'e'
result = (hak > 0) and (devam == 'e')  # Sonuç : False olur.


# Or Operatörü 
# True, True olduğu zaman sonuç True dur.
# True, False olduğu zaman sonuç True olur.
# False, False olduğu zaman sonuç False olur.

result = (x > 0) or (x % 2 == 0)  # x = 5 için True,False dan cevap True gelir.


# Not Operatörü 
result = (x > 0)  # Sonuç True çıkacaktır.


# Ancak not operatörünü kullanırsak sonuç tam tersi çıkacaktır.
result = not(x > 0)  # True olan sonucu False yaptık.


# ÖRNEK :
  # x, 5-10 arasında olan çift bir sayı mıdır ?
result = (x > 5) and (x < 10) and (x % 2 == 0)  # x = 5 olduğu için sonuç False çıkar.
result = (x > 5) or (x < 10) and (x % 2 == 0)   # True and False sonucundan solayı cevap False çıkar.

print(result)
