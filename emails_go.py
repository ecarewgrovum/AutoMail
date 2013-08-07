import csv

def messagegen(aList):
	message = """Dear %s,
	
Your email address is %s
You are %s
You have %s book(s) checked out
Wild Wild West

-------------------------------
""" % (aList[0], aList[1], aList[2], aList[3])
	return message

with open('verification_emails_0806.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		if counter != 0: # if not header row
			with open('cop_emails.txt', 'a+') as textfile:
				textfile.write(messagegen(x))
		else:
			counter += 1
		
		

