mydict = dict()
print(mydict)
mydict = {'Name': 'John', 'Age': 37}
print(mydict)

mydict = dict(Name='John', Age=37, isMale=True)
print(mydict)

print(mydict['Age'])

print("---------")

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])

print("---------")

mydict = {str(i * 2) : i for i in range(1,10)}
print(mydict)

mydict = {'Name': 'Noname', 'Age': -1}
Name = input("Введите имя: ")
Age = input("Введите возраст: ")
mydict = {'Name': Name, 'Age': Age}
for key in mydict:
    print(key, '=', mydict[key])

