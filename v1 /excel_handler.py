import openpyxl
import database

worksheet = openpyxl.Workbook()
sheet = worksheet.active 


sheet.append(['نام','دسته بندی','قیمت','زمان','توضیحات'])
for item in database.show() : 
    sheet.append(item)

worksheet.save('Export.xlsx')
