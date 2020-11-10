if 3>2:
     print('Hoş Geldiniz')

if 3>3:
     print('Hoş Geldiniz')    # Sistem yazmaz ! FALSE 

if 3==3:
     print('Hoş Geldiniz')    # Hoş Geldiniz yazar.
if True:
     print('Hoş Geldiniz')    # Hoş Geldiniz yazar.
if False:
     print('Hoş Geldiniz')    # Sistem yazmaz ! FALSE 

isLoggedin = True
if isLoggedin:
     print('Hoş Geldiniz')    # Hoş Geldiniz yazar.
isLoggedin = False
if isLoggedin:
     print('Hoş Geldiniz')   # Sistem yazmaz ! FALSE

username = 'sinemcan'
password = '12345'

# isLoggedin = (username == 'sinemcan') and (password == '12345')
# if isLoggedin:
#      print('Hoş Geldiniz')   # Hoş Geldiniz yazar.

if (username == 'sinemcan') and (password == '12345'):  # şeklinde de yazılabilir.
     print('Hoş Geldiniz')    # Hoş Geldiniz yazar.

if (username == 'sinemcann') and (password == '12345'):
    print('Hoş Geldiniz')
else: 
     print('username ya da parola yanlış')   # username yanlış olduğu için else için tanımlanan yazar !

if (username == 'sinemcan'):
     if (password == '12345'):
          print('Hoş Geldiniz')
     else:
          print('Parola yanlış')
else:
     print('username yanlış')    # Tüm bilgiler TRUE olduğu için sistem Hoş Geldiniz yazar !

if (username == 'sinemcann'):
     if (password == '12345'):
          print('Hoş Geldiniz')
     else:
          print('Parola yanlış') 
else:
     print('username yanlış')    # Username yanlış olduğu için username yanlış yazılmıştır.

if (username == 'sinemcan'):
     if (password == 123455):
          print('Hoş Geldiniz')
     else:
          print('Parola yanlış')
else:
     print('username yanlış')
