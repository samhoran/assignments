from datetime import datetime

raw_date = "1-May-12"
#-d doesn't work on my computer with strptime (it's
#fine with strftime), but some googling/trying it and
#seeing what happens tells me that strptime works fine
#with %d even for non-zero-padded
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") 
print(date_str)