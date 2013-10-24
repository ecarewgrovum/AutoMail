import csv

def messagegen(aList):
	message = """To: %s

Subject: Chronicle of Philanthropy Endowment Report Verification: RESPOND BY FRIDAY, NOV. 1
 
%s 

Friday, October 25, 2013

Dear %s, 

For our 2013 report on Endowments, I want to verify the following five data points for publication in order to ensure we are publishing the correct figures for your organization.

Please respond by Friday, Nov. 1st.  If we do not hear from you by then, we will publish what you have already provided. Thank you for helping us ensure accuracy.

 

Fiscal Year 2011 Market Value of Endowment:  $%s
Fiscal Year 2012 Market Value of Endowment:  $%s

YTD Market Value of Endowment and date of estimate: $%s as of %s

Return on Investment for FY 2012: %s percent

 

Thanks again,
-------------------
""" % (aList[1], aList[7], aList[0], aList[3], aList[2], aList[4], aList[5], aList[6])
	return message

with open('End_emails_test.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		if counter != 0: #if not header row
			with open('End_emails_test_1024.txt', 'a+') as textfile:
		else:
		counter += 1
