import pytest
from hesap_makinesi import toplama, çıkarma, çarpma, bölme

def test_toplama():
    assert toplama(2, 3) == 5

def test_çıkarma():
    assert çıkarma(10, 4) == 6

def test_çarpma():
    assert çarpma(3, 3) == 9

def test_bölme():
    assert bölme(10, 2) == 5

def test_sifira_bolme():
    with pytest.raises(ZeroDivisionError):
        bölme(10, 0)

def test_carpma_negatif():
    assert çarpma(-2, 3) == -6