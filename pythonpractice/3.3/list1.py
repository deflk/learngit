school = []
school.append('tshinghua')
school.append('pku')
school.append('whu')
school.insert(2,'hust')
print(school)
del school[1]
print(school)
school.insert(1,'bupt')
print(school)
school.remove('bupt')

print(sorted(school))
print(sorted(school,reverse=True))
print(school)
school.sort()
print(school)
school.sort(reverse=True)
print(school)
print(len(school))
school.pop()
school.pop()
school.pop()
print(school)
