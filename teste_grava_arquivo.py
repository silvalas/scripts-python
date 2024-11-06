import datetime
import json

def coletar_dados_usuario(id):
    """Coleta dados do usuário e retorna um dicionário."""
    nome = input("Nome: ")
    if nome == 'xx':
        return {'nome': nome}
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
    cidade = input("Cidade: ")
    return {'id': id, 'nome': nome, 'idade': idade, 'cidade': cidade}

def salvar_dados_json(dados_usuarios, nome_arquivo):
    """Salva os dados em um arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
        print(f"\n*******************************************\nArquivo '{nome_arquivo}' gravado com sucesso!\n*******************************************\n")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    #data_proc = datetime.date.today().strftime("%Y%m%d")
    data_proc = 20241031
    caminho_arq = r"C:\Users\lesan\Documents\Curso Python\OO"
    nome_arquivo = caminho_arq + r'\teste-'+ f'{data_proc}.json'

    lista_usuarios = []
    i = 0
    #for i in range(1):
    while True:
        i+=1
        print(f"\n----- Registro {i} -----")
        usuario = coletar_dados_usuario(i)
        if usuario['nome'] == 'xx':
            break
        else:
             lista_usuarios.append(usuario)

    salvar_dados_json(lista_usuarios, nome_arquivo)

if False:

#############  Início do código comentado  #############
### Obs.: Código feito na mão, pegando sugestões do Gemini para comandos de data, aceitação de caracteres especiais e formatação do Json

    import datetime
    import json

    data_proc = datetime.date.today().strftime("%Y%m%d")
    caminho_arq = r"C:\Users\lesan\Documents\Curso Python\OO"
    nome_arq = r'\teste-'
    formato_arq = '.json'

    nome_arquivo = caminho_arq + nome_arq + data_proc + formato_arq

    def grava_arquivo(lista):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
            return f'****************************************\nArquivo gravado com sucesso!\n****************************************'

    lista = []
    cont = 1

    while cont < 5:
        print(f'---------------------\nRegistro {cont}\n---------------------')
        nome = input('Nome: ')
        idade = int(input('Idade = '))
        cidade = input('Cidade = ')
        lista.append({'nome': nome, 'idade': idade, 'cidade': cidade})
        cont += 1

    print(grava_arquivo(lista))

#############  Final do código comentado  #############