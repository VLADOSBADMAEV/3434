# Вывод строки в терминал
# \t - знак табуляции позволяет проставлять проблем
# sep="" - позволяет убирать проблемы между символами
# end="" - позволяет не переносить на следующую строку
# \n = позволяет переносить на новую строку
# pow(5,2) -  функция возведение в стемень
# round (5,2) - функция округляет число к большему
# //  - округляет к меньшему
# input() - ввод текст от пользователя
# str() - функция которая приводит число к строке
# int() - приводит число к строке

numbers = [4, 3, 2, 1, 5, True, 5.6]

numbers.append(55)  # позволяет добавить новые элементы
numbers.insert(3, 5534)  # позволяет вложить элементы, указывая индекс
numbers.extend([5, 3, 4])  # позволяет добавить группа элементов
# numbers.sort() # сортирует по порядку
# numbers.reverse() # порядок идет наоборот
# numbers.remove() # удаляет определенное значение
# numbers.pop() # удаляет элемент последнего значения, если что то передать то удалит элемент по индексу
# numbers.clear() # удаляет все элементы
# numbers.count(5) - позволяет посчитать кол-во значений в списке / например сколько пятерок
# isupper() - возвращает булевое значение и определяет вся ли строка написана в верхнем регистре или нет
# find() - находит определенный элемент в слове и возвращает его индекс
# split() - позволяет разбить строку на несколько элементов
# capitalize() - возводит первую букву слова в верхний регистр
# join - обьединяет списк в строку


# print(len(numbers)) - кол-во элементов


word = 'Car,superjet,submarine'

vehicle = word.split(',')

for a in range(len(vehicle)):
    vehicle[a] = vehicle[a].capitalize()

result = ", ".join(vehicle)
print(result)

# КОРТЕЖИ  - нельзя видоизменять значения, добавлять, удалять -тотображаются с круглыми скобками ()
# Списки - используются с квадратными скобками []
# Cловари - {}


nums = [4, 22, 4]

news = tuple(nums)
print(news)

access = {'code': 'RUS','name':'Russia','population': 1600000}


#print(access.keys()) - выводит на экран только ключи
#print(access.values()) - выводит на экран только значения
#print(access.items()) - выводит на экран и ключи и значения



#access = dict(code='RU',name='Russia',population=1600000) - еще один вариант через функцию dict

#for key, val in access.items(): - перебор словаря
    #print(key,val)

person = {
    'user':{
        'first_name': 'John',
        'last_name' : 'August',
        'age' : 45,
        'address' : ['г. Элиста', 'ул Аюка', 'кв. 45'],
        'grades' : {'Алгебра': 5, 'Физика': 4}


},
    'user2': {

    }
          }


print(person['user']['grades']['Алгебра'])


# МНОЖЕСТВА / используется функция set


data = {4,2,5,2,1,4,2,2}
print(data)

nums = [4,3,2,1,4,2,2]

new_nums = set(nums)

# ФУНКЦИИ


nums1 = [6,4,3,2,1] # Находим минимальный элемент в списке



def minimal(list):
    min = list[0]
    for a in nums1:
        if a < min:
            min = a
    return min

mine= minimal(nums1)
print(mine)


# РАБОТА С ФАЙЛАМИ


#data = input("Введи ")

#file = open('new/text.txt','a') # a - append , w - write

#file.write(data + "\n")

#file.close()

file = open('new/text.txt','r') # - r - read


for a in  file:
    print(a,end="")


file.close()


# ИСКЛЮЧЕНИЯ


#try :
     #x = int(input("Введи число"))
     #x += 5
     #print(x)
#except ValueError:
    #print("Лучше введи число")

try:
    x = 5 / 0
    x = int(input())
except ZeroDivisionError:
    print("Нельзя делить на ноль")
except ValueError:
    print("Ввели текст")
finally:
    print("Хватит")


try:
    with open('folders/text.txt','r',encoding='utf-8') as file1:
        file.read()
except FileNotFoundError:
    print("Ошибка создания файла")
finally:
    file.close()


import hashlib

print('Привет','мне','нравится','программирование', sep=";")
print('но', 'писать','код', 'что-то', 'не очень.','Может поможешь',end='!')
print('\nhello kak dela','vse horosho')


print('da')