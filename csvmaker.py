import time
import os
from openpyxl import load_workbook
import csv
import sys

try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")

fileprefix = 'CSV'

def removeHeader(inputfile):

    timestr = time.strftime("%Y%m%d-%H%M")
    filename = str(fileprefix+' - '+timestr+'.csv')
    wb = load_workbook(inputfile)
    ws = wb.active
    ws.delete_rows(ws.min_row, 1)
    with open(filename, 'w', newline="") as f:
        col = csv.writer(f)
        for row in ws.rows:
            col.writerow([cell.value for cell in row])

removeHeader(droppedFile)