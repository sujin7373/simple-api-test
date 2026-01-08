import pytest

def test_addition():
    "기본성공 케이스"
    print("피카츄")
    assert 1+1 ==2
    
def no_test_addition():
    print("어니부기")
    assert 1+1 ==2
    
def test_minus() :
    print("메롱")
    assert 3-1 == 2