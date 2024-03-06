import pandas as pd
from openpyxl import Workbook

def init_excel():
    # Create a new Excel workbook
    wb = Workbook()
    
    # Create the 'Users' sheet with column headers
    ws = wb.active
    ws.title = "Users"
    ws.append(['Username', 'EmailID', 'Password'])
    
    # Save the workbook to a file
    wb.save(filename='email_server.xlsx')

if __name__ == "__main__":
    init_excel()
