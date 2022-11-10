import session_accessor
import pandas as pd
from datetime import datetime, timedelta
from numpy.random import randint
import time as t
import gc
import os


def test_df(n):
    '''
    Function creates test pandas Dataframe
    with n - number of rows,
    to test session.add_id() method.
    Function returns pandas Dataframe with 
    columns: 'customer_id','product_id','timestamp'.
    '''
    if n < 3:
        n = 3
    time_now = datetime.now().time().strftime('%H:%M:%S')
    time_now = datetime.strptime(time_now,'%H:%M:%S')
    timestamp = []
    [timestamp.append(time_now + timedelta(minutes=1)) if i == 0 else \
     timestamp.append(timestamp[-1] + timedelta(minutes=1)) 
     for i in range(10**n)]
    df = pd.DataFrame(columns=['customer_id','product_id','timestamp'])
    customer_id = randint(10,10**(n-1),size=10**n)
    product_id = randint(8*10**(n-1),9*10**(n-1),size=10**n)
    df.loc[:,'customer_id'] = customer_id
    df.loc[:,'product_id'] = product_id
    df.loc[:,'timestamp'] = timestamp
    return df


if __name__ == '__main__':
    # ENV VARS
    POWER_DEFAULT = 7
    SESSION_TIME_VAL_DFLT = 3
    SESSION_TIME_FORMAT_DFLT = 'm'
    n = int(os.getenv('POWER', POWER_DEFAULT))
    stime = int(os.getenv(
        'SESSION_TIME_VAL',
        SESSION_TIME_VAL_DFLT
    ))
    sformat = (os.getenv(
        'SESSION_TIME_FORMAT',
        SESSION_TIME_FORMAT_DFLT
    ))

    print(f'Power is {n}' if n>=3 else f'Power is set to 3')
    df = test_df(n)
    start = t.time()

    df1 =df.session.add_id(stime,sformat)
    print('#'*25, ' Sample ', '#'*25)
    print(df1.sample(10))
    print('#'*60)

    finish = t.time()
    time_spent = round((finish - start)/60,2)
    print(f'It took {time_spent} minutes to process {df.shape[0]} rows.')
    gc.collect()
