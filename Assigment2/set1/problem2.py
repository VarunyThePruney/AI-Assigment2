marks = open('marks.txt', 'w')
marks.write('Ram 85\nSita 92\nArjun 76')
marks.close()

marks = open('marks.txt', 'r')
mark = marks.read()
print(mark)