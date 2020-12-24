import pytest

def inversa_cadena(cadena):
    nueva_cadena = ''
    j = -1
    for i in range(len(cadena)):
        nueva_cadena += cadena[j]
        j -= 1
    return nueva_cadena


@pytest.mark.parametrize("cadena, output",[('hola','aloh'),('hola como estas','satse omoc aloh'),('quien eres tu','ut sere neiuq')])
def test_inversa_cadena(cadena, output):
    assert inversa_cadena(cadena) == output
