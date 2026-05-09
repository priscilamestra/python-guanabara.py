print("dicionário em python")

alunos = {}
nome = input("Nome:")
média = float(input(f"Média de {nome}:"))
alunos['nome'] = nome
alunos['média'] = média
if média >= 7:
    print(f" - nome: {alunos['nome']}\n - média: {alunos['média']}\n - situação: APROVADO.")
else:
    print(f" - nome: {alunos['nome']}\n - média: {alunos['média']}\n - situação: REPROVADO")

