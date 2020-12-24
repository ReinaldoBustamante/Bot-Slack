import pytest

@pytest.mark.parametrize("num, output",[('[4,7,3,9,5]',3),('[2,3,4,6,5]',2)])
def test_get_min_value(num, output):
    assert get_min_value(num) == output

def get_min_value(lista) :
    if (lista[0] == '[' and lista[-1] == ']') :
        i = 1
        min = int(lista[1])
        while lista[i] != ']':
            if lista[i] != ',':
                if int(lista[i]) <= min:
                    min = int(lista[i])
                i += 1
            if lista[i] != ']':
                i += 1
        return min
    else:
        print('usted no esta ingresando una lista')

lista = '[1,2,3,4]' 
print(get_min_value(lista))

