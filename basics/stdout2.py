import sys
sys.stdout.write("Hello\n")

sys.stdout = open('hello.dat', 'a')
print("World")

textfile = open('test.dat','a')
print('Hello Testfile', file=textfile)
