import csv

def messagegen(aList):
	message = """To: %s

Hi %s
Thanks so much for taking the time to complete our Chronicle of Philanthropy survey of executive compensation. 

We're taking active steps this year to ensure the data is double-checked early in the process.

If you could please take a few minutes to verify the data below, that would help us tremendously. These are the responses that will guide the key components of our analysis and will be printed in the paper and online. 

Chief executive officer in 2011 and 2012: %s, %s
Total taxable compensation 2011: $%d
Total nontaxable benefits 2011: $%d
Total compensation 2011: $ %d

Total taxable compensation 2012: $%d
Total nontaxable benefits 2012: $%d
Total compensation 2012: $%d

Highest paid employee who is not the CEO in 2011 and 2012:%s
Total taxable compensation 2011: $%d
Total nontaxable benefits 2011: $%d
Total compensation 2011: $%d

Total taxable compensation 2012: $%d
Total nontaxable benefits 2012: $%d
Total compensation 2012: $%d

I've also attached a copy of your full responses for your records. Please review it and let us know if any of your data need to be changed. 

Many thanks for your assistance, 

-------------------------------
""" % (aList[4], aList[0], aList[10], aList[3])
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
		
		

