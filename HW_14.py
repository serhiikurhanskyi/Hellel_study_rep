from functools import wraps
from datetime import datetime


def measure_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      start = datetime.now()
      res = func(*args, **kwargs)
      end = datetime.now()
      delta = end - start
      print(func.__name__, str(delta))
      return res
    return wrapper


@measure_exec_time
def gen_list_dicts(n=0):
    lst = []
    for i in range(n + 1):
        lst.append({j: j ** 2 for j in range(i + 1)})
    return lst


for i in range(5):
    print(gen_list_dicts(i))

lst_1 = list(range(1, 11))
lst_2 = list(range(11, 21))
lst_3 = list(range(21, 31))


lst_1, lst_3 = (filter(lambda x: not x % 2, lst) for lst in (lst_1, lst_3))
lst_2 = filter(lambda x: x % 2, lst_2)

lst_union = zip(lst_1, lst_2, lst_3)
lst_sum = map(sum, lst_union)
lst_sum_odd = list(filter(lambda x: x % 2, lst_sum))
print(lst_sum_odd)
