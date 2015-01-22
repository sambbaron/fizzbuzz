# First version of FizzBuzz

n = 30

print "Fizz buzz counting up to {}".format(n)

for a in range(1,n+1):
  if a % 3 == 0 and a % 5 == 0:
    print "fizzbuzz"
  elif a % 3 == 0:
    print "fizz"
  elif a % 5 == 0:
    print "buzz"
  else:
    print a  
