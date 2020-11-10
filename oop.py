# class 
# instance (object)  kavramları bizim için önemli !

lst1 = [1,2,3]
lst2 = [1,2,3,4]

result = type(lst1)
result = type(lst2)
print(result)
# Sonuç : <class 'list'>  şeklinde gelecektir.

# Liste içinde oluşturulmuş metodları instance üzerinden kullanabilirim.

# class ==> Person(name,surname,birthday,calculateAge())
# (Örneğin; uygulamada kullanıcı kaydı tutucaz.)
# Bu tür işlemleri sadece 1 kişi için yapıcak olsak bir class'a ihtiyacımız yok. Ancak bu işlemleri birçok
# kişiye yapılacağı için class oluşturulur.

# Person class'ını oluşturup bu class üzerinden tanımlayacak olduğumuz her bir obje bir instance bizim bu
# bilgileri tutabilmemizi sağlayacak. Böylelikle class içindeki instance bilgilere metot olarak ulaşabilicez.

