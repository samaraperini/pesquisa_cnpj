import navegador
import time
import captcha

site_consulta = "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao_CS.asp"
xpath_nome = "/html/body/div[1]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td/table[3]/tbody/tr/td/font[2]/b"
    
def consulta_cnpj(driver,numero_cnpj):
    navegador.acessar_url(driver, site_consulta)
    campo_cnpj = navegador.aguardar_clicavel(driver,"//input[@id='cnpj']", tempo_espera=10)
    for char in numero_cnpj:
        campo_cnpj.send_keys(char)
        time.sleep(0.1)
    navegador.escrever(campo_cnpj,numero_cnpj)
    imagem_captcha = navegador.aguardar_clicavel(driver,"//img[@id='imgCaptcha']", tempo_espera=60)
    campo_captcha = navegador.encontrar_elemento(driver, "//input[@id='txtTexto_captcha_serpro_gov_br']")
    captcha.salvar_captcha(imagem_captcha, 'captcha.png')  
    resposta_captcha = captcha.resolver_captcha('captcha.png')    
    navegador.clicar(campo_captcha)
    navegador.escrever(campo_captcha,(resposta_captcha['code']))
    consultar = navegador.encontrar_elemento(driver, "//button[@type='submit']")
    navegador.clicar(consultar)   

    
         
