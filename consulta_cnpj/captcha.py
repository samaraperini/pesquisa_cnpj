import os
from anticaptchaofficial.imagecaptcha import imagecaptcha
from selenium.webdriver.remote.webelement import WebElement

def salvar_captcha(element: WebElement, local_arquivo: str):
        with open (local_arquivo, 'wb') as img:
            img.write(element.screenshot_as_png)

def resolver_captcha(local_arquivo: str):
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(os.getenv('ANTICAPTCHA'))
    resultado = solver.solve_and_return_solution(local_arquivo)
    if resultado != 0:
        resposta = {'code': resultado, 'task_id': solver.task_id}
        return resposta
    else:
        raise Exception(f'Erro ao tentar resolver captcha de imagem pela antiCaptcha - {solver.error_code} - {solver.err_string}')
