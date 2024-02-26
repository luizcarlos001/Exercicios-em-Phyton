n = int(input("Crie uma senha de 4 dígitos: "))

if n < 9999:
    print("Senha registrada")
else:
    print("A senha deve conter 4 dígitos")

s = int(input("Digite a senha registrada anteriormente: "))

if s == n:
    print("Senha correta")
else:
    print("Senha incorreta")