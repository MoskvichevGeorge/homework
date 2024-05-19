grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
GPA = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4]))
print(GPA)
order = sorted(students)
print(order)
Klass = {order[0]:GPA[0],order[1]:GPA[1],order[2]:GPA[2],order[3]:GPA[3],order[4]:GPA[4]}
print(Klass)