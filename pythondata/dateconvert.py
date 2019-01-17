from datetime import datetime

def convertdate(raw_date):
	date_format = "%Y-%m-%d"


	#Read date; note parsed_date is a date type
	parsed_date = datetime.strptime(raw_date, date_format)



	#Note strf not strp; note date_str is a string
	date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
	return date_str

print(convertdate("2017-01-11"))
print(convertdate("2007-05-06"))
print(convertdate("1900-10-30"))


#note to self: zero-padded means there's a zero in front