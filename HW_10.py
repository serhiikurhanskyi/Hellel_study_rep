# Дано список словорей
# [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# создать список кортежей
# [('red', 'high'), ('yellow', 'low')]
lst = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
tuples = [(d['color'], d['value']) for d in lst]

# Дано словарь
# a_dictionary = {"a": 1, "b": 2, "c": 3}
# преобразовать его в список кортежей
# [('a', 1), ('b', 2), ('c', 3)]

a_dictionary = {"a": 1, "b": 2, "c": 3}
d = [(k, v) for k, v in dict.items(a_dictionary)]

# Дано два списка
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# Создать из них список кортежей
# list_c = [(1,5), (2,6), (3,7), (4,8)]

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list(zip(list_a, list_b))


# Дано словарь
# {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
# Создать кортеж значений для первих трьох єлементов словоря

d_ = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
ld = list(d_.items())
ld.pop(3)
t_ = tuple(ld)


# Дано список
# ["bar", "baz", "qux", "etc"]
# Создать кортеж
# ("foo", "bar", "baz", "qux", "etc")

lst = ["bar", "baz", "qux", "etc"]
lst.append("foo")
last_el = lst.pop(-1)
lst.insert(0, last_el)
t = tuple(lst)
