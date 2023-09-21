from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(6)) == 2*6
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4*5
