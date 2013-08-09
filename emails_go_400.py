import csv

def messagegen(aList):
	message = """To: %s
	
Text: %s

Hi %s
Thanks soTurtles turls

ensation. 

We're taking active steps this year to ensure the data is double-checked early in the process.

If you could please take a few minutes to verify the data below, that would help us tremendously. These are the responses that will guide the key components of our analysis and will be printed in the paper and online. 

Chief executive officer in 2011 and 2012: %s, %s
Total taxable compensation 2011: $%s
Total nontaxable benefits 2011: $%s
Total compensation 2011: $ %s

Total taxable compensation 2012: $%s
Total nontaxable benefits 2012: $%s
Total compensation 2012: $%s

Highest paid employee who is not the CEO in 2011 and 2012:%s, %s
Total taxable compensation 2011: $%s
Total nontaxable benefits 2011: $%s
Total compensation 2011: $%s

Total taxable compensation 2012: $%s
Total nontaxable benefits 2012: $%s
Total compensation 2012: $%s

I've also attached a copy of your full responses for your records. Please review it and let us know if any of your data need to be changed. 

Many thanks for your assistance, 

-------------------------------
""" % (aList[2], aList[0], aList[1], aList[3], aList[7], aList[11], aList[12], aList[14], aList[15], aList[16], aList[18], aList[19], aList[23], aList[27], aList[28], aList[30], aList[31], aList[32], aList[34])
	return message

with open('salaryverificationemails_0807.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		if counter != 0: # if not header row
			with open('400_emails.txt', 'a+') as textfile:
				textfile.write(messagegen(x))
		else:
			counter += 1
		
		

