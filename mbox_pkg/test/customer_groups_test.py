# Libraries
import pytest
from functions import *

# Test Data
testdata_qnt = {'datatype': [('1',1.2, {}),(1.2, 4, {}), (2, 1.2, {}),
                             ('1', 0, {}), (11, '2', {}), ('1','5', {}),
                             ([123], 5, {}), ([22], [0], {}), 
                             ([2],[5], {}), ((7, 2), 4, {}), 
                             ((3), (3,1), {}), 
                             ((3), (4), {4: 1, 5: 1, 6: 1})],
                'values_positive': [(0, 0, {}), (0, 5, {}),
                                    (-1, 5 , {}),
                                    (-2, -5, {}),
                                    (1, -5, {}),
                                    (4, 0, {0: 1, 1: 1, 2: 1, 3: 1}),
                                    (30, 0, {0: 1, 1: 2, 2: 3, 3: 3, 4: 3, 
                                             5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 
                                             10: 2, 11: 1}),
                                    (25, 11, {2: 2, 3: 3, 4: 3, 5: 3,
                                              6: 3,7: 3, 8: 3, 9: 2, 
                                              10: 2, 11: 1})],
                'values_negative': [(-7, 4, {1: 1, 2: 1, 3: 1}),
                                    (4, 0, {0: 2, 1: 1, 2: 1}),
                                    (11, 15, {6: 2, 7: 1, 8: 1, 9: 1, 10: 1, 
                                              2: 1, 3: 1, 4: 1, 5: 2})]}
testdata_num = {'datatype': [('123', 6), (55.2, 12), (10, 1)],
                'values_positive': [(0, 0), (1, 1), (157, 13)],
                'values_negative': [(-124, 7), (-124, 5)]}
testdata_qnt0 = {'datatype': [('2', {}), (1.2, {}), ([12], {}), 
                              ((2,2), {}), ((2),{0: 1, 1: 1})],
                 'values_positive': [(2, {0: 1, 1: 1}), 
                                     (7, {0: 1, 1: 1, 2: 1, 
                                     3: 1, 4: 1, 5: 1, 6: 1})],
                 'values_negative': [(-8, {0: 1, 1: 1, 2: 1, 3: 1,
                                           4: 1, 5: 1, 6: 1, 7: 1})]}


# Test Functions
class TestCustomerGroupsByQnt:
    
    @pytest.mark.parametrize("n_customers,n_first_id,expected",
                             testdata_qnt['datatype'],
                             scope='function')
    def test_datatype(self,n_customers,n_first_id,expected):
        assert groups_by_qnt(n_customers,n_first_id) == expected
        assert groups_by_qnt_np(n_customers,n_first_id) == expected
    
    
    @pytest.mark.parametrize("n_customers,n_first_id,expected",
                             testdata_qnt['values_positive'],
                             scope='function')
    def test_values_positive(self,n_customers,n_first_id,expected):
         assert groups_by_qnt(n_customers,n_first_id) == expected
         assert groups_by_qnt_np(n_customers,n_first_id) == expected
    
    
    @pytest.mark.parametrize("n_customers,n_first_id,expected",
                             testdata_qnt['values_negative'],
                             scope='function')
    def test_values_negative(self,n_customers,n_first_id,expected):
         assert groups_by_qnt(n_customers,n_first_id) != expected
         assert groups_by_qnt_np(n_customers,n_first_id) != expected


    @pytest.mark.parametrize("n_customers,expected",
                             testdata_qnt0['datatype'],
                             scope='function')
    def test_datatype0(self,n_customers,expected):
        assert groups_by_qnt_zero_id(n_customers) == expected
    
    
    @pytest.mark.parametrize("n_customers,expected",
                             testdata_qnt0['values_positive'],
                             scope='function')
    def test_values_positive0(self,n_customers,expected):
         assert groups_by_qnt_zero_id(n_customers) == expected
    
    
    @pytest.mark.parametrize("n_customers,expected",
                             testdata_qnt0['values_negative'],
                             scope='function')
    def test_values_negative0(self,n_customers,expected):
         assert groups_by_qnt_zero_id(n_customers) != expected


class TestCountNum:
    
    @pytest.mark.parametrize("num,expected",
                             testdata_num['datatype'],
                             scope='function')
    def test_num_datatype(self, num, expected):
        try:
            assert count_num(num) == expected
        except:
            with pytest.raises(ValueError) as err:
                raise ValueError(err)
    

    @pytest.mark.parametrize("num,expected",
                             testdata_num['values_positive'],
                             scope='function')
    def test_num_values_positive(self, num, expected):
        assert count_num(num) == expected
    
    
    @pytest.mark.parametrize("num,expected",
                             testdata_num['values_negative'],
                             scope='function')
    def test_num_values_negative(self, num, expected):
        with pytest.raises(Exception):
            assert count_num(num) != expected
        

        
        
