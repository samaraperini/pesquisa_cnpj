#imports
import os
import pandas as pd
import iniciar
import driver
import navegador
import coletar_dados
#caminho_arquivos
INPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
CAMINHO_INPUT = os.path.join(INPUT_PATH, 'input.csv')

driver = driver.abrir_navegador()
df_input = pd.read_csv(CAMINHO_INPUT)
consultas = df_input['CNPJs']

for numero_cnpj in consultas:
    iniciar.consulta_cnpj(driver,numero_cnpj)    
    try:
        navegador.aguardar_clicavel(driver,iniciar.xpath_nome)
    except Exception as e:
        print('Erro ao consultar cnpj', numero_cnpj)
        for tentativas in range(0,1):
            try:
                iniciar.consulta_cnpj(driver,numero_cnpj)   
                navegador.aguardar_clicavel(driver,iniciar.xpath_nome)
            except Exception as error:
                print('Erro ao consultar CNPJ', numero_cnpj, 'consulta finalizada.')
                break
            else: coletar_dados.coletar_dados(driver,numero_cnpj)
    else:
        coletar_dados.coletar_dados(driver,numero_cnpj)
#criando_output
df_output = pd.DataFrame.from_dict(coletar_dados.dicionario)
df_output.drop_duplicates(subset=['CNPJ'], inplace=True)
df_output.drop([0], axis=0, inplace=True)
df_output.to_excel(f'{OUTPUT_PATH}\\output.xlsx', engine='xlsxwriter', index=False)

print('Output gerado com sucesso!')
driver.quit()
