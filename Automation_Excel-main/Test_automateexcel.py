
from openpyxl import workbook, load_workbook

import datetime


wb=load_workbook('daily_overview(FKA 2hr).xlsx')

#current_date = dt.date.today()
todays_date = str(datetime.datetime.now().strftime("%m-%d-%y"))

wb.copy_worksheet(wb.active)

#wb.title = todays_date

#print(wb.title)

wb.save('daily_overview(FKA 2hr).xlsx')

