import random

# Lista para armazenar informações dos alunos
alunos = []


# Função para calcular a média da escola
def calcular_media(notas):
    return sum(notas) / len(notas) if len(notas) > 0 else 0


# Função para verificar a porcentagem da bolsa com base na renda familiar
def verificar_porcentagem_bolsa(renda_familiar):
    match renda_familiar:
        case x if x < 1400:
            return 100
        case x if x < 2800:
            return 50
        case x if x < 4200:
            return 30
        case _:
            return 0


# Função para determinar a escolaridade com base na idade usando match
def determinar_escolaridade(idade):
    match idade:
        case x if x < 6:
            return "Pré-Escolar"
        case 6, 7:
            return f"{idade - 5}º ano do Ensino Fundamental"
        case 8:
            return "2º ano do Ensino Fundamental"
        case 9:
            return "3º ano do Ensino Fundamental"
        case 10:
            return "4º ano do Ensino Fundamental"
        case 11:
            return "5º ano do Ensino Fundamental"
        case 12:
            return "6º ano do Ensino Fundamental"
        case 13:
            return "7º ano do Ensino Fundamental"
        case 14:
            return "8º ano do Ensino Fundamental"
        case 15:
            return "9º ano do Ensino Fundamental"
        case 16:
            return "1º ano do Ensino Médio"
        case 17:
            return "2º ano do Ensino Médio"
        case 18:
            return "3º ano do Ensino Médio"
        case _:
            return "Fora da escolaridade regular"


# Função para verificar se o aluno passou no ENEM
def verificar_aprovacao_enem(nota_enem):
    return "Apto" if nota_enem > 500 else "Não Apto"


# Função principal para cadastrar alunos
def cadastrar_alunos():
    while True:
        matricula = random.randint(1000, 9999)
        nome = input("Digite o nome do aluno: ")
        sobrenome = input("Digite o sobrenome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        email = input("Digite o email do aluno: ")
        renda_familiar = float(input("Digite a renda familiar do aluno: "))
        filiacao = input("Digite a filiação do aluno: ")
        cpf = input("Digite o CPF do aluno: ")

        # Determinar automaticamente a escolaridade com base na idade
        escolaridade = determinar_escolaridade(idade)

        # Solicitar a nota do ENEM
        nota_enem = int(input("Digite a nota do aluno no ENEM: "))

        # Calcular a média da escola
        notas = [nota_enem]
        media_escola = calcular_media(notas)

        # Verificar a porcentagem da bolsa
        porcentagem_bolsa = verificar_porcentagem_bolsa(renda_familiar)

        # Dicionário com as informações do aluno
        aluno_info = {
            "Matrícula": matricula,
            "Nome": f"{nome} {sobrenome}",
            "Idade": idade,
            "Email": email,
            "Renda Familiar": renda_familiar,
            "Filiação": filiacao,
            "CPF": cpf,
            "Escolaridade": escolaridade,
            "Nota ENEM": nota_enem,
            "Resultado ENEM": verificar_aprovacao_enem(nota_enem),
            "Resultado Média Escola": media_escola,
            "Porcentagem da Bolsa": porcentagem_bolsa
        }

        # Adicionar o dicionário à lista de alunos
        alunos.append(aluno_info)

        # Exibir informações armazenadas no dicionário
        print("\nInformações do Aluno:")
        for key, value in aluno_info.items():
            print(f"{key}: {value}")

        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break


# Chamada da função para cadastrar alunos
cadastrar_alunos()

# Imprimir o conteúdo da lista de alunos em uma única linha
print("\nConteúdo da Lista de Alunos:")
for aluno in alunos:
    print("\n---")
    print(
        f"Matrícula: {aluno['Matrícula']}, Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Email: {aluno['Email']}, Renda Familiar: {aluno['Renda Familiar']}, Filiação: {aluno['Filiação']}, CPF: {aluno['CPF']}, Escolaridade: {aluno['Escolaridade']}, Nota ENEM: {aluno['Nota ENEM']}, Resultado ENEM: {aluno['Resultado ENEM']}, Resultado Média Escola: {aluno['Resultado Média Escola']}, Porcentagem da Bolsa: {aluno['Porcentagem da Bolsa']}")

# Imprimir o nome da lista
print("\nNome da Lista: alunos")