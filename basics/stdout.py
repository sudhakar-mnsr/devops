import sys
sys.stdout.write("Hello\n")
sys.stdout = open("stdout.dat", "a")
print("Hello")
textfile = open("test.dat", "a")
#print >> textfile,'hello'
print('hello', file=textfile)
print("END")
