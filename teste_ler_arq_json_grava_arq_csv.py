import json
import csv
import codecs
import os

def ler_arquivo_json(endereco_arq_json):
    """Leitura do arquivo JSON e carrega dados em uma lista de dicionários."""
    try:
         # Verifica se o arquivo existe
        if not os.path.exists(endereco_arq_json):
            raise FileNotFoundError()

        with codecs.open(endereco_arq_json, 'r', encoding='utf-8-sig') as arquivo_json:
            dados_json = json.load(arquivo_json)
          # Verifica se o arquivo está vazio
            if not dados_json:
                raise ValueError()

            print(f'\nMSG 03 - Arquivo {endereco_arq_json} lido com sucesso!')
            return dados_json
    
    except FileNotFoundError as e:
        print(f"\nMSG 01 - Arquivo não encontrado no diretório: {endereco_arq_json}\nDescrição do erro: {e}")
        return None

    except ValueError as e:
        print(f"\nMSG 02 - O arquivo '{endereco_arq_json}' está vazio.\nDescrição do erro: {e}")
        return None

    except Exception as e:
        print(f"\nMSG 04 - Erro ao tentar ler o arquivo '{endereco_arq_json}'.\nDescrição do erro: {e}")
        return None  # Retorna None em caso de erro

def gravar_dados_csv(endereco_arq_csv, dados_json):
    """Gravação de arquivo CSV, guardando o valor do conjunto de chave-valor 
    de cada registro do arquivo JSON."""    
    try:
        with open(endereco_arq_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
            reg_saida = csv.writer(arquivo_csv, delimiter=';')
            reg_saida.writerow(['ID', 'Nome', 'Idade', 'Cidade'])
            for registro in dados_json:
                reg_saida.writerow(registro.values())
            print(f'\nMSG 05 - Arquivo {endereco_arq_csv} gravado com sucesso!\n')
            return None
            
    except Exception as e:
        print(f"\nMSG 06 - Erro ao tentar gravar o arquivo '{endereco_arq_csv}'.\nDescrição do erro: {e}")		   

def proc_principal():
    """Função principal do programa, onde ocorrem as chamadas de leitura e gravação dos arquivos."""
    #data_proc = datetime.date.today().strftime("%Y%m%d")
    data_proc = 20241031
    diretorio_arq = r"C:\Users\lesan\Documents\Curso Python\OO"
    endereco_arq_json = diretorio_arq + r'\teste-'+ f'{data_proc}.json'
    endereco_arq_csv = diretorio_arq + r'\teste-arq-json-para-csv-'+ f'{data_proc}.csv'

    dados_entrada = ler_arquivo_json(endereco_arq_json)

    if dados_entrada:
        gravar_dados_csv(endereco_arq_csv, dados_entrada)
    else:
        print(f'\nMSG 07 - Dados não encontrados para gravar no arquivo csv.\n')

if __name__ == "__main__":
    proc_principal()