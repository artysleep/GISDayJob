some_list = [7, 14, 28, 32, 32, '56']

def custom_filter(some_list):
    div_seven = list(filter(lambda x:type(x) is int and x%7==0,some_list))
    return sum(div_seven)<83

some_str = 'Я - последняя буква в алфавите!'

# def anonymous_filter(some_str:str):
#     ja_lst = len(list(filter(lambda x:x.lower() == 'я',some_str)))>=23
#     return ja_lst


# Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном случае.
anonymous_filter = lambda x: True if x.count('я')+x.count('Я') > 23 else False


print(anonymous_filter('Я - последняя буква в алфавите!'))

#print(custom_filter(some_list))