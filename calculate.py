import circle
import square

''' Задаём все возможные фигуры и их функции '''
figs = ['circle', 'square']
funcs = ['perimeter', 'area']

''' Словарь для хранения размеров фигур '''
sizes = {}

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    '''Запрашиваем данные пока не станут корректными'''
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    '''Запускаем вспомогательную функцию'''
    calc(fig, func, size)