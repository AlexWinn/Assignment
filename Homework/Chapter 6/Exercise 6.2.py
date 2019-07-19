# Write a program that asks the user for the name of a file. The program should display only
# the first five lines of the file’s contents. If the file contains less than five lines, it should
# display the file’s entire contents

name = input("Enter your desired file name:")

my_file = open(name, 'r')

my_file.close()

my_file.write('1:\n')
my_file.write('2:\n')
my_file.write('3:\n')
my_file.write('4:\n')
my_file.write('5:\n')

if i in (name):

main()