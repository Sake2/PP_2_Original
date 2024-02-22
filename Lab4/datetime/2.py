from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=1)
print("Yesterday : ", new_date.strftime("%Y-%m-%d"))
new_date = current_date + timedelta(days=0)
print("Today : ", new_date.strftime("%Y-%m-%d"))
new_date = current_date + timedelta(days=1)
print("Tomorow : ", new_date.strftime("%Y-%m-%d"))
