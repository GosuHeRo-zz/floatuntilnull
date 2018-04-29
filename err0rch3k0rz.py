import sys
print ("What is your current body weight?")
body_weight = raw_input()
if 'int' not in str(type(body_weight)):
    print ("Please input a number")
    sys.exit(1)
print ("So your body weight is, " + body_weight + ", would you like to know your current bmi and if it needs to be managed?")
response = raw_input()
if response == "yes":
    print ("Let's get started")
else:
    print ("Well come back when you're ready for it")
       
print ("Enter your height")
height = raw_input()
print ("So your height is, " + height + " and your weight is, " + body_weight + " correct?")
response_dos = raw_input()
if response_dos == "yes":
    print ("ok here is your bmi")
    print (int(body_weight)/int(height))
else:
    print("Let's re-enter your height and weight")

