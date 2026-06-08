from arquivoum import somar, multiplicar


def test_somar():
    assert somar(2, 3) == 5


def test_multiplicar():
    assert multiplicar(4, 5) == 20