#!/usr/bin/python

''' string class basic method
@author vk hooda
@created 01/14/2017'''

def main():
	strlen('hello')

def strlen(inputstr):
	print 'string length ' + str(len(inputstr))
	replacestr(inputstr)

def replacestr(inputstr):
	print 'string replaced '+inputstr +' by ' + inputstr.replace(inputstr,'hello python')
	findstr(inputstr)

def findstr(inputstr):
	print 'find character in string ' + str(inputstr.find('l'))
	joinstr(inputstr)

def joinstr(inputstr):
	joinedstr = 'joined string ' + inputstr + ' world ' + 'you'.join([' and welcome ',' !!!'])
	print joinedstr
	lowerandupperstr(joinedstr)

def lowerandupperstr(inputstr):
	print 'lower case string - ' + inputstr.lower()
	print 'upper case string - '.upper() + inputstr.upper()
	slicestr('hello friend')

def slicestr(input):
	print 'slice hello friend from 1 to 5 index ' + input[1:5]
	print 'slice hello friend 1 to end index ' + input[1:]
	

if __name__ == '__main__':
	main()