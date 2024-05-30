def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')


print_params()
print_params(5)
print_params(b='новая строка')
print_params(c=False)

print_params(b=25)
print_params(c=[1, 2, 3])


def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')


values_list = [10, 'новая строка', False]
values_dict = {'a': 100, 'b': 'еще одна строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, 'еще одна новая строка']

print_params(*values_list_2, 42)
