import pytest

@pytest.mark.parametrize("num, output",[(0,0),(1,1),(2,1),(3,2),(4,3),(5,5),(6,8),(7,13),(8,21)])
def test_fibobonacci(num, output):
    assert fibonacci(num) == output


def fibonacci(n):
    serie = [0,1]
    if n > 1:
        for i in range(n-1):
            serie.append(sum(serie[-2:]))
        return serie[-1]
    if n == 0:
        return serie[0]
    if n == 1:
        return serie[1]
    else:
        return 'ingrese un numero mayor e igual que 0'


        