import pdfplumber
import pandas as pd
import zipfile
import os

nomeCsv = "tabela_extraida.csv"

def extrairTabela():
    caminhoPdf = os.path.abspath(os.path.join("..", "Teste 1", "Anexos", "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"))

    if not os.path.exists(caminhoPdf):
        print("Erro: O arquivo não foi encontrado!")
        return

    tabelasExtraidas = []

    with pdfplumber.open(caminhoPdf) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                tabelasExtraidas.extend(tabela)

    if not tabelasExtraidas:
        print("Nenhuma tabela encontrada no PDF!")
    else:
        pdf = pd.DataFrame(tabelasExtraidas).dropna(how='all')

        pdf.to_csv(nomeCsv, index=False, header=False, encoding='utf-8-sig')

        print("Tabela extraída com sucesso!")

def salvarZip():
    diretorioAtual = os.getcwd()

    if not os.path.exists(nomeCsv):
        print("Erro: O arquivo não existe. Não é possível criar o ZIP.")
        return

    with zipfile.ZipFile('Teste_Matheus_Damacena.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(os.path.join(diretorioAtual, nomeCsv), nomeCsv)

        print("Zipado com sucesso!")

def atualizarColunas():
    caminhoCsv = os.path.join("tabela_extraida.csv")

    if not os.path.exists(caminhoCsv):
        print("Erro: O arquivo não foi encontrado!")
        return

    substituicoes = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    try:
        df = pd.read_csv(caminhoCsv)

        # Substituir as abreviações nas colunas
        df.replace(substituicoes, inplace=True)

        # Salvar as alterações sobrescrevendo o arquivo original
        df.to_csv(caminhoCsv, index=False)

        print("Arquivo atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar o arquivo CSV: {e}")

extrairTabela()
salvarZip()
atualizarColunas()
