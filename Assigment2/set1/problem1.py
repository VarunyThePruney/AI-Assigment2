names = open('names.txt', 'w')
for i in range(5):
    name = input('Enter a name: ')
    names.write(name + '\n')
names.close()