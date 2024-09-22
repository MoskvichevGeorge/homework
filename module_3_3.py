def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')
print_params()
print_params(10)
print_params(20, 'новая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'текст', False]
values_dict = {'a': 7, 'b': 'другой текст', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, 'пример']
print_params(*values_list_2, 42)
