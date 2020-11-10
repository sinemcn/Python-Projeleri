myList = [1,2,3]
print(len(myList))

class Movie():
     def __init__(self,title,director,duration):
          self.title = title
          self.director = director
          self.duration = duration
          print('Movie objesi oluşturuldu.')
     def __str__(self):
          return f"{self.title} by {self.director}"

     def __len__(self):
          return self.duration
     def __del__(self):
          print('film objesi silindi.')

m = Movie('film adı','yönetmen adı',120)
# print(len(m))

# Sonuç olarak; 
# 3
# Movie objesi oluşturuldu.
# 120  gelecektir.
# film objesi silindi.

print(str(m))

# Movie objesi oluşturuldu.
# film adı by yönetmen adı  sonucu gelir.
# film objesi silindi.

# EĞER BİR OBJEYİ SİLMEK İSTERSEM ; 
del m
