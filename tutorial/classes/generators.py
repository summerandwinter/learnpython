def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

for char in reverse('golf'):
	print(char)

sum(i*i for i in range(10))  #sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))  #dot product

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(91)}
print(sine_table)

page = ['I love program', 'I love python']
unique_words = set(word for line in page for word in line.split())
print(unique_words)

graduates = [{'gpa':10,'name':'summer'},{'gpa':20,'name':'winter'}]
valedictorian = max((student['gpa'], student['name']) for student in graduates)
print(valedictorian)

data = 'golf'
reve = list(data[i] for i in range(len(data)-1, -1, -1))
print(reve)