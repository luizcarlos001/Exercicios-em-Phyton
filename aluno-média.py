nome = input("Qual é o seu nome? ")

n1 = float(input("Digita a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

m = (n1+n2+n3)/3

print("A média de {} é {}." .format (nome, m))

if m >= 7:
    r = "APROVADO"
else:
    r = "REPROVADO"

print("O Aluno {} cuja média é {} está {}" .format(nome, m, r))