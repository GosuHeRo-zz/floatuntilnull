print ("What is your current body weight?")
body_weight = input()
print ("So your body weight is, " + body_weight + ", would you like to know your current bmi and if it needs to be managed?")
response = input()
if response == "yes":
    print ("Let's get started")
else:
    print ("Well come back when you're ready for it")
       
print ("Enter your height")
height = input()
print ("So your height is, " + height + " and your weight is, " + body_weight + " correct?")
response_dos = input()
if response_dos == "yes":
    print ("ok here is your bmi")
    print (int(body_weight)/int(height))
else:
    print("Let's re-enter your height and weight")

