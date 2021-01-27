d = {'name': 'Alex', 'age': 35}
print(d)
d.setdefault('isWorking', True)
print(d)
print(d.get('age'))
d.pop('name')
print(d)
print("--------")
keys = list(d.keys())
print(keys)
print(keys[0])

values = list(d.values())
print(values)
print(values[0])

d['age'] = 40
d['isMale'] = True
print(d)
print('---------------------')
import random
d = {'hello': 'Привет', 'bye': 'Пока', 'lesson': 'Урок'}
keys = list(d.keys())
while True:
    n = random.randrange(1,4)
    if n == 1:
        print(d['hello'])
        translate = input('Введите перевод, show или quit: ')
        if translate.lower() == keys[0]:
            continue
        elif translate.lower() == 'show':
            print(d)
            exit(0)
        elif translate.lower() == 'quit':
            exit(0)
        else:
            print("Неверно")
            translate = input('Введите снова: ')
            if translate.lower() == keys[2]:
                continue
    elif n == 2:
        print(d['bye'])
        translate = input('Введите перевод, show или quit: ')
        if translate.lower() == keys[1]:
            continue
        elif translate.lower() == 'show':
            print(d)
            exit(0)
        elif translate.lower() == 'quit':
            exit(0)
        else:
            print("Неверно")
            translate = input('Введите снова: ')
            if translate.lower() == keys[2]:
                continue
    elif n == 3:
        print(d['lesson'])
        translate = input('Введите перевод, show или quit: ')
        if translate.lower() == keys[2]:
            continue
        elif translate.lower() == 'show':
            print(d)
            exit(0)
        elif translate.lower() == 'quit':
            exit(0)
        else:
            print("Неверно")
            translate = input('Введите снова: ')
            if translate.lower() == keys[2]:
                continue






