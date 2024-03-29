from datetime import datetime
date1 = datetime(2024, 2, 21, 12, 0, 0)  
date2 = datetime.now()  


date_difference = date1 - date2


difference_in_seconds = date_difference.total_seconds()

print("Difference between the two dates in seconds:", difference_in_seconds)
