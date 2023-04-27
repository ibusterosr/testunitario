import codigo

def test_suma():
    assert codigo.suma(1,1)==2
    assert codigo.suma(0,-1)==-1

def test_resta():
    assert codigo.resta(1,1)==0
    assert codigo.resta(0,-1)==1