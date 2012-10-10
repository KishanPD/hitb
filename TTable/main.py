import xlrd

book = xlrd.open_workbook('myfile.xls')

print book.nsheets
print book.sheet_names()

sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols

for rownum in range(sh.nrows):
    for i in sh.row_values(rownum):
        print i
