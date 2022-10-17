# Libraries
import numpy as np


# Functions
def groups_by_id(customer_id:int,n_first_id:int=0) -> dict:
    '''
    Функция используется для подсчета числа
    покупателей, попадающих в каждую из групп
    [группа - сумма цифр в ID покупателя].
    На вход функция получает 2 параметра:
    customer_id - ID покупателя, до которого[включительно] ведется 
                  подсчет групп и их значений
    n_first_id - начальное значение ID покупателя, с которого[включительно]
               ведется подсчет групп и их значений
    Функция возвращает словарь: {"группа":"число покупателей в группе"}.
    Если хоть один из входных параметров не соответствует типу int,
    то функция возвращает пустой словарь: {}.
    Если хоть один из входных параметров отрицательный, то
    функция возвращает пустой словарь: {}.
    Если  значение customer_id меньше значения n_first_id, то
    происходит обмен значениями, и функция формирует группы 
    покупателей на отрезке [customer_id,n_first_id], а не 
    на отрезке [n_first_id, customer_id], как предполагается изначально.
    
    '''
    # data type check
    if not (isinstance(customer_id,int) and isinstance(n_first_id,int)):
        return {}
    elif customer_id < 0 or n_first_id < 0:
        return {}
    groups = {}
    [groups.update({count_num(i):1}) if count_num(i) not in groups.keys() 
     else groups.update({count_num(i):groups[count_num(i)]+1}) \
    for i in range(n_first_id,customer_id+1)]
    return groups


def count_num(num:int) -> int:
    '''
    Функция используется для подсчета суммы цифр
    целого(int) числа 
    num - исходное число
    Функция возвращает значение суммы цифр числа num.
    Если число num не относится к целым(int), то
    функция возвращает -1.
    '''
    if not isinstance(num, int):
        msg = f'Допустимы только целочисленные значения \n\
            ("{type(num)}" - было использовано).'
        raise TypeError(msg)
    elif num < 0:
        msg = f'Допустимы только целочисленные ПОЛОЖИТЕЛЬНЫЕ(включая 0) \n\
            значения("{num}" - было использовано).'
        raise ValueError(msg)
    return sum([int(i) for i in list(str(num))])


def groups_by_qnt(n_customers:int,n_first_id:int=0) -> dict:
    '''
    Функция используется для подсчета числа
    покупателей, попадающих в каждую из групп
    [группа - сумма цифр в ID покупателя].
    На вход функция получает 2 параметра:
    n_customers - количество покупателей, которые сортируются по группам
    n_first_id - начальное значение ID покупателя, с которого[включительно]
               ведется подсчет групп и их значений
    Функция возвращает словарь: {"группа":"число покупателей в группе"}.
    Если хоть один из входных параметров не соответствует типу int,
    то функция возвращает пустой словарь: {};
    Если n_first_id отрицательный, а n_customers неположительный, то
    функция возвращает пустой словарь: {}.
    
    '''
    # data type check
    if not (isinstance(n_customers,int) and isinstance(n_first_id,int)):
        return {}
    elif n_customers <= 0 or n_first_id < 0:
        return {}
    groups = {}
    [groups.update({count_num(i):1}) if count_num(i) not in groups.keys() 
     else groups.update({count_num(i):groups[count_num(i)]+1}) \
    for i in range(n_first_id,n_first_id+n_customers)]
    return groups


def groups_by_qnt_zero_id(n_customers:int) -> dict:
    '''
    Функция используется для подсчета числа
    покупателей, попадающих в каждую из групп
    [группа - сумма цифр в ID покупателя].
    На вход функция получает 1 параметр:
    n_customers - количество покупателей, которые сортируются по группам
    начиная с ID = 0.
    Функция возвращает словарь: {"группа":"число покупателей в группе"}.
    Если входнй параметр n_customers не соответствует типу int,
    то функция возвращает пустой словарь: {}.
    Если входной параметр n_customers неположительный, то
    функция возвращает пустой словарь: {}.
    
    '''
    # data type check
    if not isinstance(n_customers,int):
        return {}
    elif n_customers <= 0 :
        return {}
    groups = {}
    [groups.update({count_num(i):1}) if count_num(i) not in groups.keys() 
     else groups.update({count_num(i):groups[count_num(i)]+1}) \
    for i in range(0,n_customers)]
    return groups


def groups_by_qnt_np(n_customers:int,n_first_id:int=0) -> dict:
    '''
    Функция используется для подсчета числа
    покупателей, попадающих в каждую из групп
    [группа - сумма цифр в ID покупателя].
    На вход функция получает 2 параметра:
    n_customers - количество покупателей, которые сортируются по группам
    n_first_id - начальное значение ID покупателя, с которого[включительно]
                ведется подсчет групп и их значений
    Функция возвращает словарь: {"группа":"число покупателей в группе"}.
    Если хоть один из входных параметров не соответствует типу int,
    то функция возвращает пустой словарь: {};
    Если n_first_id отрицательный, а n_customers неположительный, то
    функция возвращает пустой словарь: {}.
    '''
    # data type check
    if not (isinstance(n_customers,int) and isinstance(n_first_id,int)):
        return {}
    elif n_customers <= 0 or n_first_id < 0:
        return {}
    arr = np.arange(n_first_id,n_first_id+n_customers)
    pattern = lambda x: count_num(int(x))
    vfunc = np.vectorize(pattern)
    arr = vfunc(arr)
    keys, values = np.unique(arr, return_counts=True)
    return dict(zip(keys,values))

