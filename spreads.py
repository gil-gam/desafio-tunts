import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('challenge-tunts-625b57f25be6.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1NbkOelk6-TwQCZ8iDjy15pLVJOPn9InVPUSZRXQevis')
worksheet = wks.get_worksheet(0)


if int(worksheet.cell(4,3).value) > 15:
    worksheet.update_cell(4,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(4,4).value)) + int((worksheet.cell(4,5).value)) + int((worksheet.cell(4,6).value)))/3

    if m >= 70:
        worksheet.update_cell(4,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(4,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(4,7, 'Exame Final')
        worksheet.update_cell(4,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(4,8, 0)


if int(worksheet.cell(5,3).value) > 15:
    worksheet.update_cell(5,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(5,4).value)) + int((worksheet.cell(5,5).value)) + int((worksheet.cell(5,6).value)))/3

    if m >= 70:
        worksheet.update_cell(5,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(5,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(5,7, 'Exame Final')
        worksheet.update_cell(5,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(5,8, 0)


if int(worksheet.cell(6,3).value) > 15:
    worksheet.update_cell(6,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(6,4).value)) + int((worksheet.cell(6,5).value)) + int((worksheet.cell(6,6).value)))/3

    if m >= 70:
        worksheet.update_cell(6,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(6,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(6,7, 'Exame Final')
        worksheet.update_cell(6,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(6,8, 0)


if int(worksheet.cell(7,3).value) > 15:
    worksheet.update_cell(7,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(7,4).value)) + int((worksheet.cell(7,5).value)) + int((worksheet.cell(7,6).value)))/3

    if m >= 70:
        worksheet.update_cell(7,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(7,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(7,7, 'Exame Final')
        worksheet.update_cell(7,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(7,8, 0)


if int(worksheet.cell(8,3).value) > 15:
    worksheet.update_cell(8,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(8,4).value)) + int((worksheet.cell(8,5).value)) + int((worksheet.cell(8,6).value)))/3

    if m >= 70:
        worksheet.update_cell(8,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(8,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(8,7, 'Exame Final')
        worksheet.update_cell(8,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(8,8, 0)


if int(worksheet.cell(9,3).value) > 15:
    worksheet.update_cell(9,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(9,4).value)) + int((worksheet.cell(9,5).value)) + int((worksheet.cell(9,6).value)))/3

    if m >= 70:
        worksheet.update_cell(9,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(9,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(9,7, 'Exame Final')
        worksheet.update_cell(9,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(9,8, 0)


if int(worksheet.cell(10,3).value) > 15:
    worksheet.update_cell(10,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(10,4).value)) + int((worksheet.cell(10,5).value)) + int((worksheet.cell(10,6).value)))/3

    if m >= 70:
        worksheet.update_cell(10,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(10,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(10,7, 'Exame Final')
        worksheet.update_cell(10,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(10,8, 0)


if int(worksheet.cell(11,3).value) > 15:
    worksheet.update_cell(11,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(11,4).value)) + int((worksheet.cell(11,5).value)) + int((worksheet.cell(11,6).value)))/3

    if m >= 70:
        worksheet.update_cell(11,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(11,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(11,7, 'Exame Final')
        worksheet.update_cell(11,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(11,8, 0)


if int(worksheet.cell(12,3).value) > 15:
    worksheet.update_cell(12,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(12,4).value)) + int((worksheet.cell(12,5).value)) + int((worksheet.cell(12,6).value)))/3

    if m >= 70:
        worksheet.update_cell(12,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(12,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(12,7, 'Exame Final')
        worksheet.update_cell(12,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(12,8, 0)


if int(worksheet.cell(13,3).value) > 15:
    worksheet.update_cell(13,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(13,4).value)) + int((worksheet.cell(13,5).value)) + int((worksheet.cell(13,6).value)))/3

    if m >= 70:
        worksheet.update_cell(13,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(13,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(13,7, 'Exame Final')
        worksheet.update_cell(13,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(13,8, 0)


if int(worksheet.cell(14,3).value) > 15:
    worksheet.update_cell(14,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(14,4).value)) + int((worksheet.cell(14,5).value)) + int((worksheet.cell(14,6).value)))/3

    if m >= 70:
        worksheet.update_cell(14,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(14,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(14,7, 'Exame Final')
        worksheet.update_cell(14,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(14,8, 0)


if int(worksheet.cell(15,3).value) > 15:
    worksheet.update_cell(15,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(15,4).value)) + int((worksheet.cell(15,5).value)) + int((worksheet.cell(15,6).value)))/3

    if m >= 70:
        worksheet.update_cell(15,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(15,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(15,7, 'Exame Final')
        worksheet.update_cell(15,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(15,8, 0)


if int(worksheet.cell(16,3).value) > 15:
    worksheet.update_cell(16,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(16,4).value)) + int((worksheet.cell(16,5).value)) + int((worksheet.cell(16,6).value)))/3

    if m >= 70:
        worksheet.update_cell(16,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(16,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(16,7, 'Exame Final')
        worksheet.update_cell(16,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(16,8, 0)


if int(worksheet.cell(17,3).value) > 15:
    worksheet.update_cell(17,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(17,4).value)) + int((worksheet.cell(17,5).value)) + int((worksheet.cell(17,6).value)))/3

    if m >= 70:
        worksheet.update_cell(17,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(17,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(17,7, 'Exame Final')
        worksheet.update_cell(17,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(17,8, 0)


if int(worksheet.cell(18,3).value) > 15:
    worksheet.update_cell(18,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(18,4).value)) + int((worksheet.cell(18,5).value)) + int((worksheet.cell(18,6).value)))/3

    if m >= 70:
        worksheet.update_cell(18,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(18,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(18,7, 'Exame Final')
        worksheet.update_cell(18,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(18,8, 0)


if int(worksheet.cell(19,3).value) > 15:
    worksheet.update_cell(19,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(19,4).value)) + int((worksheet.cell(19,5).value)) + int((worksheet.cell(19,6).value)))/3

    if m >= 70:
        worksheet.update_cell(19,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(19,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(19,7, 'Exame Final')
        worksheet.update_cell(19,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(19,8, 0)


if int(worksheet.cell(20,3).value) > 15:
    worksheet.update_cell(20,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(20,4).value)) + int((worksheet.cell(20,5).value)) + int((worksheet.cell(20,6).value)))/3

    if m >= 70:
        worksheet.update_cell(20,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(20,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(20,7, 'Exame Final')
        worksheet.update_cell(20,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(20,8, 0)


if int(worksheet.cell(21,3).value) > 15:
    worksheet.update_cell(21,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(21,4).value)) + int((worksheet.cell(21,5).value)) + int((worksheet.cell(21,6).value)))/3

    if m >= 70:
        worksheet.update_cell(21,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(21,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(21,7, 'Exame Final')
        worksheet.update_cell(21,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(21,8, 0)


if int(worksheet.cell(22,3).value) > 15:
    worksheet.update_cell(22,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(22,4).value)) + int((worksheet.cell(22,5).value)) + int((worksheet.cell(22,6).value)))/3

    if m >= 70:
        worksheet.update_cell(22,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(22,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(22,7, 'Exame Final')
        worksheet.update_cell(22,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(22,8, 0)


if int(worksheet.cell(23,3).value) > 15:
    worksheet.update_cell(23,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(23,4).value)) + int((worksheet.cell(23,5).value)) + int((worksheet.cell(23,6).value)))/3

    if m >= 70:
        worksheet.update_cell(23,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(23,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(23,7, 'Exame Final')
        worksheet.update_cell(23,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(23,8, 0)


if int(worksheet.cell(24,3).value) > 15:
    worksheet.update_cell(24,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(24,4).value)) + int((worksheet.cell(24,5).value)) + int((worksheet.cell(24,6).value)))/3

    if m >= 70:
        worksheet.update_cell(24,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(24,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(24,7, 'Exame Final')
        worksheet.update_cell(24,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(24,8, 0)


if int(worksheet.cell(25,3).value) > 15:
    worksheet.update_cell(25,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(25,4).value)) + int((worksheet.cell(25,5).value)) + int((worksheet.cell(25,6).value)))/3

    if m >= 70:
        worksheet.update_cell(25,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(25,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(25,7, 'Exame Final')
        worksheet.update_cell(25,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(25,8, 0)


if int(worksheet.cell(26,3).value) > 15:
    worksheet.update_cell(26,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(26,4).value)) + int((worksheet.cell(26,5).value)) + int((worksheet.cell(26,6).value)))/3

    if m >= 70:
        worksheet.update_cell(26,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(26,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(26,7, 'Exame Final')
        worksheet.update_cell(26,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(26,8, 0)


if int(worksheet.cell(27,3).value) > 15:
    worksheet.update_cell(27,7, 'Reprovado por Falta')
else:
    m = (int((worksheet.cell(27,4).value)) + int((worksheet.cell(27,5).value)) + int((worksheet.cell(27,6).value)))/3

    if m >= 70:
        worksheet.update_cell(27,7, 'Aprovado')
    elif m < 50:
        worksheet.update_cell(27,7, 'Reprovado por Nota')
    elif m >= 50 < 70:
        worksheet.update_cell(27,7, 'Exame Final')
        worksheet.update_cell(27,8, '5 <= (m + naf)/2')
    else:
        worksheet.update_cell(27,8, 0)