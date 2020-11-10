# GLOBAL VE LOCAL DEĞİŞKENLER 

x = 'global x'

def function():
     x = 'local x'
function()
print(x)

# Biz burada; x değişkenini tanımlıyoruz ve bir fonksiyon içerisine yine aynı x değişkeninden fonksiyon 
# kapsamında tanımlıyoruz. Fonksiyon çalıştırmak için fonksiyonu çağırıyoruz ve print ile x'i yazdırıyoruz.
# Sonuç: global x ==> GELİR.

# Fonksiyon içinde x'i değiştirmeme rağmen sonuç global x olarak gelir.Bunun nedeni; siz fonksiyon içinde yeni
# bir çalışma alanı hazırlasanız bile,fonksiyonun içindeki x değeri (local) dışarıdaki x değişkenini etkilemez.
# Bu yüzden global değişkende herhangi bir güncelleme olmaz ! Çünkü local değişkeni sisteme yazdırmak için 
# print(x) ifadesi kullanılmamıştır.

# Fonksiyonun içindeki x ifadesini print ile yazdıralım ve sonuca bakalım.
x = 'global x'
def function():
     x = 'local x'
     print(x)
function()
print(x)

# Sonuç: local x
#        global x şeklinde gelecektir.

# Eğer fonksiyon içinde herhangi bir tanımlama yapmadıysam;
x = 'global x'

def function():
     print(x)

function()
print(x)
# Sonuç:
# global x 
# global x  şeklinde gelir.Çünkü fonksiyon kapsamında olan bir tanımlama yok.Dolayısıyla fonksiyon bir üstteki
#           kapsamı kullanır.Değişken tanımlandığında tanımlanan değişken yazdırılır.

##########################################################################################

name = 'Çınar'

def changeName(new_name):
     name = new_name
     print(name)
changeName('Ada')
print(name) 
# Sonuç: Ada
#        Çınar şeklinde gelir.

# Eğer iç içe fonksiyonlar tanımlarsak bu işlem nasıl olur ? 
name = 'global string'

def greeting():
     name = 'Çınar'

     def hello():
          print('Hello '+ name)
     hello()
greeting()
# Sonuç: Hello Çınar bilgisi gelir. Fonksiyon içinde tanımlı olan name, global stringden Çınar a güncellendiği
# için ve fonksiyon print ile yazdırıldığından sonuç Hello Çınar gelir.

# Eğer ikinci fonksiyon içine bir name değişkeni tanımlar ve yazdırmak istersek;
name = 'global string'

def greeting():
     name = 'Çınar'

     def hello():
          name = 'Ada'
          print('Hello '+ name)
     hello()
greeting()
# Sonuç: Hello Ada gelecektir. Çınar bilgisi Ada bilgisiyle güncellenecektir.

# Fonksiyonların içine herhangi bir name değeri tanımlamazsak;
name = 'global string'

def greeting():

     def hello():
          print('Hello '+ name)
     hello()
greeting()
# Sonuç: Hello global string gelecektir. Çünkü hello fonksiyonu kapsamında bir name değeri yok.Bir üste çıkar.
# Bir üstte de fonksiyon kapsamında bir name değeri yoktur. Dolayısıyla en üstteki global string name bilgisi
# sisteme yazdırılır.

#############################################################################################
# Başka bir fonksiyon tanımlayalım.
x = 50 
def test(x):
     print(f'x: {x}')

     x = 100
     print(f'changed x to {x}')
test(x)
# Sonuç: x: 50
#        changed x to 100 şeklinde gelir.
# Bu durumda sadece fonksiyonu yazdırdım.Dışarıdan gelen x değişkenini yazdırmadım.test(x) fonksiyonunu
# print ile yazdırdım.

# Eğer dışarıdan gelen x değişkenini de yazdırmak istersem ;
x = 50
def test(x):
     print(f'x: {x}')

     x = 100
     print(f'changed x to {x}')
test(x)
print(x) 
# Sonuç: x: 50 
#        changed x to 100
#        50  sonuçları gelecektir.

# Eğer dışarıda global olarak tanımlanan bir değişkeni fonksiyon içerisinden değiştirmek istiyorsak şu yapılır.
x = 50
def test():
     global x 
     print(f'x: {x}')

     x = 100
     print(f'changed x to {x}')
test()
print(x)

# Sonuç :
# x: 50
# changed x to 100
# 100  sonucu gelecektir.Global olarak çağırılan x değeri önce 50,daha sonra 100 olarak geldi.
#      Bunun nedeni fonksiyon içine global olarak tanımladığımız x bilgisi dışarıda tanımlanan x'i kullanıyor
#      ve x üzerinde yapılan her değişim dışarıdaki x'i etkiler,dışarıdaki x üzerinde değişim yapılır.

name = 'Çınar'

def changeName(new_name):
     global name
     name = new_name 
     print(name)
changeName('Ada')
print(name)   
# Sonuç : 
# Ada
# Ada şeklinde gelecektir.  

# Bu durumda fonksiyona global name şeklinde gönderdiğimiz Ada bilgisi, 
# (name = 'Çınar') bilgisini (name = 'Ada') olarak güncelleyecektir.
