
print "Hi" ,
print "Sahiti"

print "Hello, What is your name?"
user=input()
print "Well ," + user + " , I'm thinking of a number between 1 and 20 . \n . Take a guess."
import random
n=int((20*random.random())+1)
m=input()
o=1
while (o<=6):
	if (m==n):
		print "	Well done " + user + " You guessed the number in " + str(o) + "guesses"
		break 
	else :
		if(m>n):
			print "Your guess is too high. \n Take a guess ."
		else:
			print "Your number is too low.\n Take a guess ."
	m=input()
	o=o+1
if (o>6):	
	print " Sorry " + user +" you were not able to guess the number.. Well, you can give it another try..Good luck.."	


