options = ['Subway', 'Bicycle', 'Motorcycle', 'Bus', 'Walk']
message = "I would like to own a Honda " + options[2].lower() + "."
print(message)


options[0] = 'boat'
print(options[0])
options.append('Carrier')
print(options)
options.insert(2, 'Airplane')
print(options)
del options[1]
print(options.pop())
print(options)
a = options.pop(1)
print(a)
too_slow = 'Walk'
options.remove(too_slow)
print(options)
print(too_slow + " is too slow for me.")
