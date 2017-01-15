#!/usr/bin/python -tt

''' Print hello world and python world welcome you
@author vk hooda
@create 01/14/2017'''

def main():
     printhello()

def printhello():
	print '-' * 30 + 'OUTPUT START' + '-' * 30
	print 'Hello Python world!'
	print 'Welcome VK Hooda in Python world! :) \n'
	print 'Important : Never forget to add this line at top : #!/usr/bin/python -tt . It use python interprator to execute this file.'
	print '-' * 30 + 'OUTPUT END' + '-' * 30

if __name__== '__main__':
	main()