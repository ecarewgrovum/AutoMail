import csv

def messagegen(aList):
	message = """To: %s

Subject: Chronicle of Philanthropy's Endowment Report Verification: PLEASE RESPOND BY WEDNESDAY, NOV. 6
 
%s 
Monday, November 4, 2013

Dear %s, 

For our 2013 report on Endowments, I want to verify the following data points for publication in order to ensure we are publishing the correct figures for your organization.

If anything needs to be updated, please let us know immediately.  If we do not hear from you by Wednesday, November 6th, we will publish what you have already provided. Thank you for helping us ensure accuracy.

Fiscal Year 2011 Market Value of Endowment:  $%s
Fiscal Year 2012 Market Value of Endowment:  $%s

YTD Market Value of Endowment and date of estimate: $%s as of %s

Return on Investment for FY 2012: %s percent

Thanks again,
-------------------
""" % (aList[1], aList[7], aList[0], aList[3], aList[2], aList[4], aList[5], aList[6])
	return message

with open('Emails_endowments_1104.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		#if not header row
		if counter != 0: 
			with open('Emails_endowments_1104.txt', 'a+') as textfile:
				textfile.write(messagegen(x))

		else:
			counter += 1
