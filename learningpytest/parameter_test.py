import pytest


@pytest.mark.parametrize("num1,num2,expected",[(1,1,2),(2,2,4),(4,4,8)])
class Testparameter:
    def test_para(self,num1,num2,expected):
        assert num1+num2==expected

    def test_para2(self,num1,num2,expected):
         assert num1+num2==expected

@pytest.mark.parametrize("num",[1,2,3,4,5])
class Testpara:
     def test_para1(self,num):
         assert num>0
         print(num)

