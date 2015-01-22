# FizzBuzz extended with user input functionality

import sys

if len(sys.argv) == 1:
  user_input = raw_input("Please enter a number for the upper bound of FizzBuzz: ")
else:
  user_input = sys.argv[1]
  
n = 0
i = 0
while n == 0:    
    try: n = int(user_input)
    except ValueError:
      if i == 0:
        user_input = raw_input("Please enter a NUMBER for the upper bound of FizzBuzz: ")
      elif i == 1:
        user_input = raw_input("A number like 1,2,3: ")
      elif i == 2:
        user_input = raw_input("Are you kidding me?  Don't you know what a number is?!: ")       
      else:
        user_input = raw_input("Dude, you're hopeless: ")       
      i += 1

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
