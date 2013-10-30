import csv

def messagegen(aList):
	message = """To: %s 
Email Subject: Please verify by January 30, 2014: Chronicle of Philanthropy's Report on Grantmaking	
Text: %s 

Hi %s

Good morning. I'm writing to ask for your help in verifying your data for our annual report on nonprofit grantmaking. 

If you could please review the fields below and let us know if any changes need to be made, that would be greatly appreciated. 

Total assets at end of FY 2013: %s
Total value of grants paid in FY 2013: $%s
Percdent change in grants paid from FY 2012: $%s
Projected giving in 2014: %s

If we do not hear back from you by January 30th, 2014, we will publish the above data that you provided. 

NOTE: THIS OBVIOUSLY USE FAKE DUMMY DATA FROM THE 2013 REPORT 

THANKS, 
SURVEY TEAM

-------------------------------
""" % (aList[1], aList[0], aList[2], aList[3], aList[4], aList[6], aList[7])
	return message

with open('Emails_Foundations_1030.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		if counter != 0: # if not header row
			with open('Emails_Foundations_1030.txt', 'a+') as textfile:
				textfile.write(messagegen(x))
		else:
			counter += 1