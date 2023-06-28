import navegador

cnpj = ['']
nome = ['']
atividadeprincipal = ['']
naturezajuridica = ['']
dicionario = {'CNPJ': cnpj , 'NOME EMPRESARIAL': nome , 'CÓDIGO E DESCRIÇÃO DA ATIVIDADE ECONÔMICA PRINCIPAL': atividadeprincipal, 'CÓDIGO E DESCRIÇÃO DA NATUREZA JURÍDICA': naturezajuridica }

xpath_nome = "/html/body/div[1]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td/table[3]/tbody/tr/td/font[2]/b"
xpath_cnpj = "/html/body/div[1]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td/table[2]/tbody/tr/td[1]/font[2]/b[1]"
xpath_atividade_principal = "/html/body/div[1]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td/table[5]/tbody/tr/td/font[2]/b"
xpath_atividade_juridica = "/html/body/div[1]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td/table[7]/tbody/tr/td/font[2]/b"

def coletar_dados(driver,numero_cnpj):
    nome_empresarial = navegador.encontrar_elemento(driver, xpath_nome).text
    cnpj_receita = navegador.encontrar_elemento(driver, xpath_cnpj).text
    atividade_principal = navegador.encontrar_elemento(driver, xpath_atividade_principal).text
    natureza_juridica = navegador.encontrar_elemento(driver, xpath_atividade_juridica).text     
    print('CNPJ',numero_cnpj,'encontrado com sucesso.')
    cnpj.append(cnpj_receita)
    nome.append(nome_empresarial)
    atividadeprincipal.append(atividade_principal)
    naturezajuridica.append(natureza_juridica)
