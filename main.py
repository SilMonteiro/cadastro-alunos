import pandas as pd
import numpy as np
import random


def gerar_df():
    
    try:
        df = pd.read_csv('alunos.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Matricula", "Nome", "Rua", "Número", "Bairro", "Cidade", "UF", "Telefone", "e-mail"])

    return df


def salvando_dados(df):

    df.to_csv('alunos.csv', index=False)

    
def numero_matricula(df):

    if df.empty:
        return 1
    else:
        return df['Matricula'].max() + 1
    

def cadastro_aluno(df):

    
    print("\n-> Para iniciar o cadastro do aluno, por favor preencha os campos abaixo:\n")
    dados_cadastro = {}
    dados_cadastro['nome'] = input("Digite o nome do aluno:").strip().lower()
    dados_cadastro['rua'] = input("Digite a rua do aluno:").strip().lower()
    dados_cadastro['numero'] = input("Digite o numero da casa do aluno:")
    dados_cadastro['bairro'] = input("Digite o bairro do aluno:").strip().lower()
    dados_cadastro['cidade'] = input("Digite a cidade do aluno:").strip().lower()
    dados_cadastro['uf'] = input("Digite a UF do aluno:").strip().lower()
    dados_cadastro['telefone'] = input("Digite o telefone do aluno:")
    dados_cadastro['email'] = input("Digite o email do aluno:").strip().lower()
    dados_cadastro['matricula'] = numero_matricula(df)

    novo_aluno_data = {
        'Matricula': [dados_cadastro['matricula']],
        'Nome': [dados_cadastro['nome']],
        'Rua': [dados_cadastro['rua']],
        'Número': [dados_cadastro['numero']],
        'Bairro': [dados_cadastro['bairro']],
        'Cidade': [dados_cadastro['cidade']],
        'UF': [dados_cadastro['uf']],
        'Telefone': [dados_cadastro['telefone']],
        'e-mail': [dados_cadastro['email']]
    }

    df_novo_aluno = pd.DataFrame(novo_aluno_data)

    df = pd.concat([df, df_novo_aluno], ignore_index=True)

    salvando_dados(df)
    print("\n-> Aluno cadastrado com sucesso!\n")
    print(df)

    saida = input("\nDigite 'S' para voltar ao menu inicial ou qualquer outra tecla para sair: ").upper()
    if saida == 'S':
        menu_inicial()

    return df


def pesquisar_aluno(df):

    pesquisa_aluno = input('\n-> PESQUISAR ALUNO - DIGITE A OPÇÃO DESEJADA:\n1 - Pesquisar pelo nome\n2 - Pesquisar pela matrícula\n').strip().lower()

     
     
def menu_inicial():

    df = gerar_df()
    print ("\n===== MENU INICIAL =====\n 1 - CADASTRAR ALUNO\n 2 - PESQUISAR ALUNO\n 3 - SAIR\n")

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("\n-> Opção inválida. Tente novamente.\n")
        menu_inicial()
        return
    
    if escolha == 1:
        df = cadastro_aluno(df)
    elif escolha == 2:
        df = pesquisar_aluno(df)
    elif escolha == 3:
        print("\n-> Saindo do sistema. Até mais!\n")
    else:
        print("\n-> Opção inválida. Tente novamente.\n")
        menu_inicial()


menu_inicial()


    




