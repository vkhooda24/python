#!/usr/bin/python

def printlist(list):
	print 'list  - ' + str(list)
	listlenght(list)

def listlenght(list):
	print 'list size ' + str(len(list))
	printlistelements(list)

def printlistelements(list):
	print 'first element - ' + list[0]
	print 'second element - ' + list[1]
	print 'third element - ' + list[2]
	printelementwithforloop(list)

def printelementwithforloop(list):
	for element in list:
		print 'element - ' + element 
	listsum([1,3,4,12])

def listsum(list):
	add = 0
	for num in list:
		add += num
	print 'total - ' + str(add)
	findinlist(['continue','done','done and bye'])

def findinlist(listitem):
	if 'done and bye' in listitem:
		print 'list operation execution done and bye !!!!'
	printnumbers(10)

def printnumbers(inputnumber):
	for i in range(inputnumber):
		print i
	whileprint(4)

def whileprint(input):
	i = 0
	while(i < input):
		i = i + input
		print i

	
# list.append('str') append element at end index in list
#list.insert(index, elem) inseart element at given index
#list.index(elem)  position of the element
#list.sort() sort a list
#list.reverse() reverse the order
#list.pop(1) remove element at given position and return element
# list.remove('curly')  search and remove that element

'''Common error: above methods do not *return* the modified list, they just modify the original list.'''


if __name__ == '__main__':
	printlist(['abc' , 'def' , 'xyz'])