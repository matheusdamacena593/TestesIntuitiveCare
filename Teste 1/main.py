import os
import time
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def downloadAqruivos():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    caminhoDownload = os.path.abspath("Anexos")

    chrome_options = Options()
    prefs = {
        "download.default_directory": caminhoDownload,
        "download.prompt_for_download": False,  # Evita a pergunta "Onde salvar?"
        "plugins.always_open_pdf_externally": True  # Baixa o PDF automaticamente sem abrir no visualizador do Chrome
    }
    chrome_options.add_experimental_option("prefs", prefs)

    navegador = webdriver.Chrome(options=chrome_options)

    navegador.get(url)

    navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click()

    xpathDownloads = ['//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]', '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a']

    for i in range(2):
        navegador.find_element(By.XPATH, xpathDownloads[i]).click()
        time.sleep(10)

    print("Download feito com sucesso!")

    navegador.quit()

def transformarZip():
    with zipfile.ZipFile('Anexos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, arquivos in os.walk('Anexos'):
            for arquivo in arquivos:
                zipf.write(os.path.join(root, arquivo))

    print("Zip Completo!")

downloadAqruivos()
transformarZip()
