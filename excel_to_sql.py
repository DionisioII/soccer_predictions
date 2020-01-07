import xlwings as xw
import csv


book = 'Sbanchiamo tutto.xlsx'

wb = xw.Book(book)

sht = wb.sheets[0]

columns=[]

query = "CREATE TABLE Matches ( id_match INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"

for i in range(4,425):
	column_value = str(sht.range('B'+str(i)).value)
	column_value = column_value.replace(" ","_")
	column_value = column_value.replace("à","a")
	column_value = column_value.replace("ò","o")
	column_value = column_value.replace("ì","i")
	column_value = column_value.replace("*","")
	column_value = column_value.replace("'","")
	column_value = column_value.replace("(","")
	column_value = column_value.replace(")","")
	column_value = column_value.replace("/","")
	column_value = column_value.replace("<","")
	column_value = column_value.replace(">","")
	column_value = column_value.replace("%","")
	column_value = column_value.replace(",","")
	column_value = column_value.replace("=","_")
	column_value = column_value[:58]
	if column_value in columns:
		if i > 205:
			column_value = column_value + "_sq2"
			while(column_value in columns):
				column_value+="1"
		else:
			column_value += "1"
			while(column_value in columns):
				column_value+="1"
	
	columns.append(column_value)

	if(column_value[0:4] != "None" ):
		query += column_value + " int, \n"

query +=" ) "

print(query)

