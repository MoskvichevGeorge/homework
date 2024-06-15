def print_params(a = 1, b = 'строка', c = True):
    print(f'a: {a}, b: {b}, c: {c}')

print_params()
print_params(10)
print_params(b = 'новая строка')
print_params(c = False)


def print_params(a = 1, b = 'строка', c = True):
    print(f'a: {a}, b: {b}, c: {c}')

values_list = [5, 'новая строка', False]
values_dict = {'a': 10, 'b': 'еще строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [7, 'еще одна строка']
print_params(*values_list_2, 42)
