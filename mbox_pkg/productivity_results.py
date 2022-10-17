# Libraries
import time
import gc
import pandas as pd
from functions import *
import matplotlib.pyplot as plt
import math

# Variables
customers_list = [10**3, 10**4, 10**5, 
                  10**6, 10**7, 10**8]
results = pd.DataFrame({'N_customers':customers_list,
                        'Runtime_LC_and_Dict':0,
                        'Runtime_NP_and_Vect': 0})

def compare():
    '''
    Тест производительности для 2-х
    вариантов функции по группировке покупателей:
    1) List Comprehansion + Dictionaries -> groups_by_qnt(n_customers)
    2) Numpy + Vectorization -> groups_by_qnt_np(n_customers)
    '''
    print('#'*50)
    print(f'List Comprehansion + Dictionaries Utilization')
    print('-'*40)
    indx = 0
    for n_customers in customers_list:
        start = time.time()
        groups = groups_by_qnt(n_customers)
        end = time.time()
        duration = round((end - start)/60,2)
        print(f'For {n_customers} it took: {duration} minutes to run.')
        results.loc[indx,'Runtime_LC_and_Dict'] = duration
        indx += 1
        gc.collect()
    print('#'*50)
    print()
    print('#'*50)
    print(f'Numpy Vectorization Utilization')
    print('-'*40)
    indx = 0
    for n_customers in customers_list:
        start = time.time()
        groups_np = groups_by_qnt_np(n_customers)
        end = time.time()
        duration = round((end - start)/60,2)
        print(f'For {n_customers} it took: {duration} minutes to run.')
        results.loc[indx,'Runtime_NP_and_Vect'] = duration
        indx += 1
        gc.collect()
    print('#'*50)
    print(results)
    plt.figure(figsize=(16,8))
    plt.plot(results.loc[:,'Runtime_LC_and_Dict'],
             (results.loc[:,'N_customers']/10**3), '-b',
             label='LC+Dict')
    plt.plot(results.loc[:,'Runtime_NP_and_Vect'],
             (results.loc[:,'N_customers']/10**3), '-r',
             label='NP+Vect')
    plt.xlabel('Runtime, minutes')
    plt.ylabel('N_Customers,Log(Thousands)')
    plt.title('Productivity Test')
    plt.legend()
    plt.show()
    return 0



if __name__ == "__main__":
    compare()