students = ['Thomas', 'Duncan', 'Ari']
students.sort()
print(students)
first_name = students[0]
first_name = first_name[:-1]
print(first_name)
sz = 0
longestName = ''
for i in students:
    if len(i) > sz:
        sz = len(i)
        longestName = i
print(longestName)
