import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('challenge-tunts-625b57f25be6.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1NbkOelk6-TwQCZ8iDjy15pLVJOPn9InVPUSZRXQevis')
worksheet = wks.get_worksheet(0)


colum = worksheet.col_values(1)
last = int(colum[-1])

lin=int(4)
for colum in range(lin, (last+4)):   
    if int(worksheet.cell(lin,3).value) > 15:
        worksheet.update_cell(lin,7, 'Reprovado por Falta')
    else:
        m = (int((worksheet.cell(lin,4).value)) + int((worksheet.cell(lin,5).value)) + int((worksheet.cell(lin,6).value)))/3
        if m >= 70:
            worksheet.update_cell(lin,7, 'Aprovado')
        elif m < 50:
            worksheet.update_cell(lin,7, 'Reprovado por Nota')
        elif m >= 50 < 70:
            worksheet.update_cell(lin,7, 'Exame Final')
            worksheet.update_cell(lin,8, '5 <= (m + naf)/2')
        else:
            worksheet.update_cell(lin,8, 0)
    lin=lin+1

