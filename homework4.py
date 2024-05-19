immutable_var = (1 , 3 , "data" , False)
print(immutable_var)
print(type(immutable_var))
immutable_var[0] = 10 #у типа tuple нет методов для добавления и удаления элементов.

mutable_list = [1 , 'base' , 'apple' , 13]
mutable_list[0] = 23
mutable_list[1] = 'grape'
mutable_list[2] = 'mushroom'
mutable_list[3] = False
mutable_list .append('ball')
print(mutable_list)
