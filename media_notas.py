nome = input("Nome: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
print("Aluno:", nome)
print("Média:", round(media, 2))

if media >= 3:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
