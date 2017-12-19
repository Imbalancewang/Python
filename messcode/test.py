import xlwt,random,xlrd
import sys
from xlutils.copy import copy
reload(sys)
sys.setdefaultencoding('utf8')
rb=xlrd.open_workbook('score2.xls')
rs=rb.sheet_by_index(0)
wb=copy(rb)
ws=wb.get_sheet(0)
ws.write(5,5,'chan')
wb.save('matthew.xls')