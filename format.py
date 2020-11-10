name = 'Çınar'
surname = 'Turan' 

print('My name is {}'.format(name))
print('My name is {} {}'.format(name, surname))
print('My name is {0} {1}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {n} {s}'.format(n=name, s=surname))
print('My name is {s} {n}'.format(n=name, s=surname))

name = 'Çınar'
surname = 'Turan'
age = 36

print('My name is {} {} and I am {} years old.'.format(name, surname, age))

# Her yere name bilgisi yazmak istersek 
print('My name is {} {} and I am {} years old.'.format(name, name, name))

# f string 

print(f'My name is {name} {surname} and I am {age} years old.'.format(name, surname, age))
