import gspread
from oauth2client.service_account import ServiceAccountCredentials
def visitor_db(visitor):
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    cred=ServiceAccountCredentials.from_json_keyfile_name('Spreadsheet-e61fd1649613.json',scope)
    gc=gspread.authorize(cred)
    wks=gc.open('Test').sheet1
    x=[]
    for i in range(0,3):
        x.append(visitor[i])
    for i in range(3,5):
        for j in range(0,2):
            x.append(visitor[i][j]) 
    #print(x)            
        
    #print(wks.get_all_records())   #To print the data of spreadsheets. It will be printed in form of a dictionery (Key-Value pair)
    wks.append_row(x)  # To append entries with data in spreadsheet
    #wks.delete_row(2)    # Delete second row
    #print(wks.get_all_records())