#1.
x = 38

print('привет')
if x < 0:
    print("Меньше нуля")
print("до свидания")
#2
a, b = 10, 5
if a > b:
    print("a > b")
if a > b and a > 0:
    print("Успех")
if (a > b) and ( a > 0 or b < 1000):
    print("Успех")
if 5 < b and b < 10:
    print("Успех")
#3
if "34" > "123":
    print("Успех")
if "123" > "12":
    print("Успех")
if [1,2] > [1,1]:
    print("Успех")
#4
if '6' > 5:
    print("Успех")
if [5,6] > 5:
    print("Успех")
if '6' != 5:
    print("Успех")
