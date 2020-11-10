message = 'Hello There. My name is Sinem Can'
print(message)

message = message.upper()  # Upper ın içine bir şey tanımlamasak bile parantezi kapatmak zorundayız. upper message içindeki karakterlerin hepsini büyük harf yazmamızı sağlayacaktır.
print(message)

message = message.lower() # Lower karakterini seçtiğimizde message karakterlerinin tümünün küçük harf yazılacağını biliriz.
print(message)

message = message.title() # Title message karakterinin içindeki kelimelerin baş harflerini büyük yazar.
print(message)

message = message.capitalize()  # Message ın içindeki kelimelerin sadece ilk kelimenin harfini büyük harfle yazar, diğer kelimelerin harfleri küçük yazılır.
print(message)

message = ' Hello There. My name is Sinem Can.'  # Hello karakterinin başına bir boşluk bıraktığımızda ilk karakter boşluk olacaktır.
print(message)

message = message.strip()  # Yazdığımızda Hello karakterinin başındaki boşluk gidecektir. # Bu işlemi uygulayarak kullanıcının girdiği baş ve sondaki boşlukkarakterler silinir.
print(message)

message = message.split()  # Bu bilgide message karakterlerinin arasındaki boşluk olan her kelime 'string' olarak ayrı ayrı yazılır. Her bir kelime boşluk karakterlerinden ayrılır.
print(message)

# Bu durumda split metoduna oluşan dizinin içindeki karakterlerin indeksine ulaşmak istersek ; ulaşmak istediğimiz indeks yazılır.
split = ['Hello', 'There.', 'My', 'name', 'is', 'Sinem', 'Can.']
print(message[0])  # 0.indeks Hello çıkacaktır.
print(message[2])  # 2.indeks My çıkacaktır.
print(message[3])  # 3.indeks name çıkacaktır.

# split parametresine herhangi bir bilgi girmezsek karakterleri boşluktan itibaren ayırır.
# Eğer split parametresine herhangi bir bilgi atarsak 
message = message.split('.') # Bu karakterleri noktadan itibaren ayır demektir.
print(message)   # Bunun sonucunda 'Hello there.' , 'My name is Sinem Can' olacaktır.
# # Noktadan sonra ayırdığımızda artık sadece 0 ve 1 bilgisine ulaşılabilinir. Bu da şu şekilde yazılır.
print(message[0]) 
print(message[1])  # olarak yazılabilir. Başka seçenek yoktur.

message = message.split()  # Bilgileri boşluktan itibaren ayırıp yazdıralım.
print(message)
# Daha sonra bunları tekrardan toplayıp eski haline getirelim. Bunun için message = ' '.join(message) yazılır. Bu aralarında bir boşluk bırakarak message karakterlerini birleştirerek yaz demektir.
message = ' '.join(message)
print(message)   # Yazdığımızda Hello There. My name is Sinem Can.  yazılacaktır.

# Örneğin aralarına boşluk ekleme '*' ekle dersek 
message = '*'.join(message) 
print(message)

message = '---'.join(message)
print(message) 

# Eğer verilen bir cümle içerisinde bir kelimeyi bulmak istersek şu işlem yapılır.
index = message.find('Sadık')
print(index)  # Eğer sonuç -1 ise message cümlesinin içinde Sadık kelimesi yok demektir.

index = message.find('Sinem')
print(index)  # Eğer sonuç aşağıdaki gibi pozitif bir sayı çıkarsa (sonuç:24) bu cümle içindeki indeks sayısını yani bu kelimenin başladığı yeri ilk harfinin olduğu yeri gösterecektir.

isFound = message.startswith('H')  # Burada yapılan şey ise cümlenin H harfiyle başlayıp başlamadığını sorma işlemidir. Message cümlesi H ile başladığı için sistem bize True cevabını verecektir.
print(isFound)

isFound = message.startswith('B')  # yaparsak bu durumda sonuç False çıkacaktır.
print(isFound)   

isFound = message.endswith('.')   #yaparsak burda da en son karakterin nokta(.) ile bittiğini mi sorarız.
print(isFound)

message = message.replace('Sinem', 'Uygar')  # Burada ilk başta yazılan kelimeyi cümle içinde bularak 2.kelimeyle değiştirme komutu veriliyor.
print(message) ##Sonuç olarak Hello There. My name is Sinem Can yerine Hello There. My name is Uygar Can. yazılır !

message = message.replace(' ', '*')
print(message)

# Replace leri özellikle url oluştururken kullanabiliriz.
message = message.replace('c','ç').replace('i','ı')  # gibi replaceleri arttırabilir bu işlemleri tek seferde yapabiliriz.
print(message)

message = message.center(100)   # Bu işlem yazılmak istenen mesajı hem sağ hem de soldan eşit aralık bırakarak tam ortaya yazar.Burada 100 er 100er iki taraftandan boşluk bırakılarak ortalanmıştır.
print(message)

message = message.center(50)
print(message)  # Bu durumda 50 karakterlik boşluk bırakılıp ortalanacaktır.

message = message.center(50, '*')  # Bu şekilde yazarsak baştan ve sondan bırakılan 50 karakterlik boşluğu görmüş oluruz ve string karakteri ortalar.
print(message)
















