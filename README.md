# desafio-tunts
Criar uma aplicação capaz de ler uma planilha do google sheets, buscar as informações necessárias, calcular e escrever o resultado na planilha.


1. Fazer o download e instalar o software Python; 

2. Criar um ambiente isolado. Na linha de comando DOS, executar:
```
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-api-python-client
```

3. Instalar a API "gspread" do Python: na linha de comando DOS, executar:  
```
pip install gspread oauth2client
```

4. Instalar uma IDE (ambiente de desenvolvimento) de sua preferência (eu utilizei o Visual Studio Code);

5. Acessar https://console.developers.google.com/project e criar um projeto. Eu criei um projeto chamado "challenge-tunts".
		5.1. Em seguida, no meu, acesse "APIs e Serviços" -  "Credenciais";
		5.2. Acesse "Chave da Conta de Serviço";
		5.3. Dê um nome à conta de serviço (eu criei o nome: project-challenge;
		5.4. Selecione: Projeto - Proprietário;
		5.5. Em "Tipo de Chave", selecione "JSON";
		5.6. Por fim, "Criar";
		5.7. No meu, acesse "Biblioteca"; na barra de pesquisa, digite: "sheets"; clique em "Google Sheets API"; clique em "Salvar";
		
6. Em seguida, criar o arquivo "spreads.py", com o seguinte conteúdo:
```
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('KEY')
worksheet = wks.get_worksheet(0)
```
		
		6.1 Copie o ID da planilha "Engenharia de Software..." (1NbkOelk6-TwQCZ8iDjy15pLVJOPn9InVPUSZRXQevis);
		6.2. Cole este ID na linha 6 do arquivo "spreads.py", substituindo a palavra 'KEY';
		6.3. Na linha de comando DOS, executar: 
```
python spreads.py
```
		6.4. Este é conteúdo básico, para acessar a planilha;
		
7. Em seguida, o arquivo "spreads.py" foi alterado, contendo todo o código para  executar as tarefas solicitadas (ver conteúdo do arquivo);

8. Para executar a aplicação, na linha de comando DOS, executar:
```
python spreads.py
```

