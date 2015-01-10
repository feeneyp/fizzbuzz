# fizzbuzz program counts up to chosen number n and prints fizz for multiples of 3 and buzz for muliples of 5
import sys

if (len(sys.argv)>=2):
  n = int(sys.argv[1])
else:
  n = int(raw_input ("How high do you want the fizzbuzz counting program to count? "))
print "OK. This fizzbuzz counting program will count up to %i" %n
for i in range(1,n+1):
  if (i%3 == 0 and i%5 != 0):
    print "fizz"
  elif (i%5 == 0 and i%3 != 0):
    print "buzz"
  elif (i%5 == 0 and i%3 == 0): 
    print "fizzbuzz"
  else:
    print i