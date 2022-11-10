import pandas as pd
import numpy as np


# products data creation
def create_data(name:str):
    '''
    Function creates products or categories data.
    Name as initial parameter defines which of 2
    will be created.
    Function returns pandas Dataframe with 
    structure: {'id':[values1],'name':[values2]}
    '''
    data_df = pd.DataFrame({'id':[],'name':[]})
    data_id = [id for id in range(1,101)]
    data_df.loc[:,'id'] = data_id
    data_df.loc[:,'name'] = name +'_' + data_df.loc[:,'id'].astype('str')
    return data_df    


def data_bind():
    '''
    Function creates data for 
    prodcategories sql table,
    returns pandas dataframe 
    with structure: {'col1':[val1], 'col2':[val2]}
    '''    
    data_df = pd.DataFrame({'col1':list(range(1,101)), 'col2':list(range(1,101))})
    data_df.loc[:,'col1'] = [None if val % 10 == 0 else val 
    for val in data_df.loc[:,'col1']]
    data_df.loc[21:29, 'col1'] = 21
    data_df.loc[41:49, 'col1'] = 41
    data_df.loc[:,'col2'] = [None if (val % 31 == 0) 
    or (val % 17 == 0) or (val % 19 ==0) else val
    for val in data_df.loc[:,'col2']]
    data_df.loc[31:39, 'col2'] = 31
    data_df.loc[71:79, 'col2'] = 71
    data_df = data_df.dropna(axis=0)
    data_df.loc[:,'col1'] = data_df.loc[:,'col1'].astype('int')
    data_df.loc[:,'col2'] = data_df.loc[:,'col2'].astype('int')
    return data_df




if __name__ == '__main__':
    prod_df = create_data(name='product')
    prod_df.to_csv('products.csv',index=False, header=False)
    cat_df = create_data(name='category')
    cat_df.to_csv('categories.csv',index=False, header=False)
    data_df = data_bind()
    data_df.to_csv('prodcategories.csv', index=False, header=False)