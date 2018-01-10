namelist = ['bill gates', 'pony ma', 'jack ma', 'alexis sanchez', 'mesut ozil']
invite = namelist[-2].title() + ", Would you like to have a diner with me ?"
print(namelist)
print(invite)
cant_attend = namelist.pop(2)
print("\n" + cant_attend.title() + " is busy to have a diner with others,so he can't keep this date,but i don't give a shit")
namelist.insert(2, 'jason bourne')
print("\nI'm glad to invite these bignames to have a diner party with me as following " + str(namelist))

namelist.append('wangzuxian')
print("\n" + str(namelist))

delname = namelist.pop(0)
print("Sorry to tell you that you can't coming, " + delname.title())

delname1 = namelist.pop(1)
print("Sorry to tell you that you can't coming, " + delname1.title())
delname1 = namelist.pop(1)
print("Sorry to tell you that you can't coming, " + delname1.title())
delname1 = namelist.pop(1)
print("Sorry to tell you that you can't coming, " + delname1.title())
print(namelist)
del namelist[0]
del namelist[0]
print(namelist)
