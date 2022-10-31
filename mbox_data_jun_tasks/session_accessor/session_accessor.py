import numpy as np

@pd.api.extensions.register_dataframe_accessor("session")
class SessionAccessor:
    def __init__(self, pandas_obj):
        self._validate_colnames(pandas_obj)
        self._validate_dtypes(pandas_obj)
        self._obj = pandas_obj   
          
            
    @staticmethod
    def _validate_colnames(obj):
        # verify there are required columns 
        if "customer_id" not in obj.columns \
        or "product_id" not in obj.columns \
        or "timestamp" not in obj.columns:
            err = '''
            DataFrame must have 'customer_id',
            'product_id' and 'timestamp' columns.
            '''
            raise AttributeError(err)
    
    
    @staticmethod
    def _validate_dtypes(obj):
        # veryfy that required columns have approprite data types
        if obj.customer_id.dtype != np.dtype(int):
            print('"customer_id" will be casted into "int" data type')
            try:
                obj['customer_id']= obj['customer_id'].astype(int)
                print('"customer_id" has been successfully casted into "int"')
            except:
                err = 'Error! "customer_id" must has "int" data type'
                raise TypeError(err)
        if obj.timestamp.dtype != np.dtype('datetime64[ns]'):
            print('"timestamp" will be casted into\
            "datetime64[ns]" data type')
            try:
                obj['timestamp']= obj['timestamp'].astype('datetime64[ns]')
                print('"timestamp" has been successfully casted into\
                "datetime64[ns]"')
            except:
                err = 'Error! "timestamp" must has "datetime64[ns]" data type'
                raise TypeError(err)
        
            
    def cast_dtypes(self,df):
        '''
        Check and convert if necessary initial
        columns to initial data types
        '''
        if df.customer_id.dtype != np.dtype(int):
            df['customer_id'] = df['customer_id'].astype(int)
        if df.product_id.dtype != np.dtype(int):
            df['product_id'] = df['product_id'].astype(int)
        if df.timestamp.dtype != np.dtype('datetime64[ns]'):
            df1['timestamp'] = df1['timestamp'] \
            .astype('datetime64[ns]')       
        return df
    
    
    def sort_by_customer_and_time(self,df):
        # sort values by customer_id and timestamp
        df['id'] = df.index.values
        df = df.sort_values(by=['customer_id','timestamp'])
        df = df.reset_index(drop=True)
        return df
    
    
    def add_previous_vals(self,df):
        '''
        Add 2 new columns to df to store customer_id's
        and timestamp's values, shifted by 1 row.
        '''
        df['customer_id_prev'] = df['customer_id'].shift(1)
        df.loc[0,'customer_id_prev'] = -1 
        df['timestamp_prev'] = df['timestamp'].shift(1)
        df.loc[0,'timestamp_prev'] = df.loc[0,'timestamp']
        df['customer_id_prev'] = df['customer_id_prev'].astype(int)
        return df
    
    
    def add_condition_cols(self,df,deltatime,timeformat):
        # add 2 new columns with boolean values
        df['customer_id_bool'] = df['customer_id'].values != \
        df['customer_id_prev'].values
        df['timestamp_bool'] = df['timestamp'].values - \
        df['timestamp_prev'].values <= \
        np.timedelta64(deltatime,timeformat)
        return df
    
    
    def session_id_col(self,df):
        # add session_id column to df
        df['session_id'] = -1
        a = [0]
        [a.append(a[-1]) if (df.loc[i,'customer_id_bool'] == False) &
         (df.loc[i,'timestamp_bool'] == True) else 
         a.append(a[-1]+1) if 
         (df.loc[i,'customer_id_bool'] == False) & 
         (df.loc[i,'timestamp_bool'] == False )
         else a.append(0) for i in df.index[1:]]
        df['session_id'] = a
        return df
    
    
    def clean_and_sort(self,df):
        # remove unnecessary df columns and reset index to initial order
        df = df.drop(columns=['customer_id_prev',
                              'timestamp_prev',
                             'customer_id_bool',
                             'timestamp_bool'])
        df.index = df['id'].values
        df.drop(columns=['id'],inplace=True)
        df = df.sort_index()
        df.reset_index(inplace=True,drop=True)
        return df
    
    
    def add_id(self,deltatime=3,timeformat='m'):
        '''
        Method adds 'session_id' column to dataframe.
        Method takes 2 parameters:
        deltatime - time span value[int value], which unites several
        'customer_id' actions to be considered inside the 
        same session;
        timeformat - time span units['Y','M','D','h','m','s']
        By default: deltatime=3, timeformat='m'.
        '''
        if self._obj.shape[0] == 0:
            return self._obj
        # df = pd.DataFrame(data=self._obj.values,
        #                   columns=self._obj.columns)
        df = self._obj.copy()
        customer_id = self._obj.customer_id
        product_id = self._obj.product_id
        timestamp = self._obj.timestamp
        
        #check and cast dtypes
        # df = self.__cast_dtypes(df)
        
        #sort by 'customer_id' and 'timestamp'
        df = self.__sort_by_customer_and_time(df)

        # add columns with previous values
        df = self.__add_previous_vals(df)

        # add bool cols
        df = self.__add_condition_cols(df,deltatime,timeformat)

        # create session_id
        df = self.__session_id_col(df)

        # clean df and sort by initial id
        df = self.__clean_and_sort(df)
        return df
    
    
    __sort_by_customer_and_time = sort_by_customer_and_time
    __add_previous_vals = add_previous_vals
    __add_condition_cols = add_condition_cols
    __session_id_col = session_id_col
    __clean_and_sort = clean_and_sort
    __cast_dtypes = cast_dtypes
   