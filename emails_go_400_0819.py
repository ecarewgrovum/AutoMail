import csv

def messagegen(aList):
	message = """To: %s, %s
	
%s

Hi %s,
Thank you so much for taking the time to complete our annual Philanthropy 400 report. 

We are taking active steps this year to ensure that key data points are double-checked early in the process. 

If you could please take a few minutes to verify the data below, that would help us tremendously. These are the responses that will guide the key components of our analysis and will be printed in the paper and online. 

Total private support, FY 2011: $%s
Total private support, FY 2012*: $%s
Total private support, FY 2013: $%s

* This is the number we use to determine the ranking of the top 400
>> Most nonprofits, this figure is equivalent with Part VIII, Line 1h minus Line 1e on the IRS Form 990. For public and private colleges and universities, this figure is equivalent to the combination of outright giving and deferred giving at present value, as reported to the Council for Aid to Education. 

Value of your private support from cash sources, FY 2011: $%s
Value of your private support from cash sources, FY 2012: $%s
Value of your private support from cash sources, FY 2013: $%s

Value of your private support from noncash sources excluding stocks, FY 2011: $%s
Value of your private support from noncash sources excluding stocks, FY 2012: $%s
Value of your private support from noncash sources excluding stocks, FY 2013: $%s

Value of your private support from noncash sources that were in the form of stocks, FY 2011: $%s
Value of your private support from noncash sources that were in the form of stocks, FY 2012: $%s
Value of your private support from noncash sources that were in the form of stocks, FY 2013: $%s

Name of your chief development officer in 2011: %s
Name of your chief development officer in 2012: %s

I've also attached a copy of your full responses for your records. Please review it and let us know if any of your data need to be changed. 

Many thanks for your assistance,

-------------------------------
""" % (aList[0], aList[1], aList[2], aList[3], aList[4], aList[5], aList[6], aList[7], aList[8], aList[9], aList[10], aList[11], aList[12], aList[13], aList[14], aList[15], aList[16], aList[17])
	return message

with open('0819_p400_emails.csv', 'rU') as csvfile:
	read = csv.reader(csvfile)
	counter = 0
	for x in read:
		if counter != 0: # if not header row
			with open('400_emails_0819.txt', 'a+') as textfile:
				textfile.write(messagegen(x))
		else:
			counter += 1
		
		

